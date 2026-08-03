"""Task 10 fixture: order-preserving duplicate removal.

Deterministic, self-contained implementation using only the Python
standard library (pure builtins, no imports required).
"""

__all__ = ["dedupe_stable"]


def dedupe_stable(items):
    """Return a new list with duplicates removed, keeping first-seen order.

    >>> dedupe_stable([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> dedupe_stable([])
    []
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
