"""Issue 06: clamp a value into [lo, hi]."""


def clamp(value, lo, hi):
    """Return *value* clamped into the inclusive range [lo, hi].

    Raises:
        ValueError: if lo > hi (invalid range).
    """
    if lo > hi:
        raise ValueError(f"invalid bounds: lo ({lo}) > hi ({hi})")
    return max(lo, min(value, hi))
