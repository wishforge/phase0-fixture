"""Issue 06: clamp a value into a closed interval."""


def clamp(value: float, lo: float, hi: float) -> float:
    """Return ``value`` restricted to the closed interval ``[lo, hi]``.

    Args:
        value: The number to clamp.
        lo: Lower bound of the interval.
        hi: Upper bound of the interval.

    Returns:
        ``value`` if ``lo <= value <= hi``, otherwise the nearest bound.

    Raises:
        ValueError: If ``lo > hi``.
    """
    if lo > hi:
        raise ValueError(f"lo ({lo}) must be <= hi ({hi})")
    return max(lo, min(value, hi))
