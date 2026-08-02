"""Issue 21: engine-owned retry policy fixture.

Deterministic, offline model of the planning stage's retry behaviour.
``retry_policy`` computes a capped exponential backoff schedule and
``run_planning_stage`` replays steps against that schedule, recording the
delays it would have waited instead of sleeping. No I/O, no clocks, no
randomness: repeated calls with the same inputs give identical results.
"""

__all__ = ["retry_policy", "run_planning_stage"]


def _require_positive_number(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number, got {value!r}")
    if value <= 0:
        raise ValueError(f"{name} must be > 0, got {value!r}")


def retry_policy(
    attempts: int,
    *,
    base_delay: float = 300,
    factor: float = 3,
    max_delay: float = 3600,
) -> list[float]:
    """Return the capped exponential backoff schedule for ``attempts`` retries.

    Each delay is ``min(base_delay * factor ** index, max_delay)`` as a float,
    with ``index`` starting at 0. ``retry_policy(3)`` therefore yields
    ``[300.0, 900.0, 2700.0]`` under the defaults.

    Raises ``ValueError`` for a non-integer or negative ``attempts``, or for
    non-positive ``base_delay``/``factor``/``max_delay``.
    """
    if isinstance(attempts, bool) or not isinstance(attempts, int):
        raise ValueError(f"attempts must be an int, got {attempts!r}")
    if attempts < 0:
        raise ValueError(f"attempts must be >= 0, got {attempts!r}")
    _require_positive_number(base_delay, "base_delay")
    _require_positive_number(factor, "factor")
    _require_positive_number(max_delay, "max_delay")

    return [
        float(min(base_delay * factor ** index, max_delay))
        for index in range(attempts)
    ]


def run_planning_stage(steps: list[str], flaky=None, policy=None) -> dict:
    """Simulate running ``steps`` with retries, without ever sleeping.

    ``flaky`` is an optional callable ``flaky(step, attempt) -> bool`` where
    ``attempt`` is the 1-based try count for that step; truthy means the step
    fails transiently and should be retried. ``policy`` is the list of allowed
    backoff delays (default ``retry_policy(3)``), shared across the stage.

    On each transient failure the next delay is appended to ``schedule`` and
    the step is retried. When the policy is exhausted the stage stops early.

    Returns ``{"status": "ok" | "failed", "attempts": int,
    "completed": list[str], "schedule": list[float]}`` where ``attempts``
    counts every step try (failures included) and ``schedule`` records the
    delays that would have been waited.
    """
    if not isinstance(steps, (list, tuple)) or not all(
        isinstance(step, str) for step in steps
    ):
        raise ValueError(f"steps must be a list of strings, got {steps!r}")
    if flaky is not None and not callable(flaky):
        raise ValueError(f"flaky must be callable or None, got {flaky!r}")
    if policy is None:
        budget = retry_policy(3)
    else:
        if not isinstance(policy, (list, tuple)):
            raise ValueError(f"policy must be a list of delays, got {policy!r}")
        budget = []
        for delay in policy:
            if isinstance(delay, bool) or not isinstance(delay, (int, float)):
                raise ValueError(f"policy delays must be numbers, got {delay!r}")
            if delay < 0:
                raise ValueError(f"policy delays must be >= 0, got {delay!r}")
            budget.append(float(delay))

    completed: list[str] = []
    schedule: list[float] = []
    attempts = 0
    pending = list(budget)

    for step in steps:
        step_attempt = 0
        while True:
            step_attempt += 1
            attempts += 1
            if flaky is not None and flaky(step, step_attempt):
                if not pending:
                    return {
                        "status": "failed",
                        "attempts": attempts,
                        "completed": completed,
                        "schedule": schedule,
                    }
                schedule.append(pending.pop(0))
                continue
            completed.append(step)
            break

    return {
        "status": "ok",
        "attempts": attempts,
        "completed": completed,
        "schedule": schedule,
    }
