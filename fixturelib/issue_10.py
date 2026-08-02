"""Issue 10: order-preserving (stable) de-duplication."""


def dedupe_stable(items):
    """Return a new list with duplicates removed, keeping first-occurrence order.

    Standard-library only; no external dependencies.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
