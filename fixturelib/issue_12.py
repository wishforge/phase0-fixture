from typing import Any


def find_first_duplicate(items: list) -> Any | None:
    """Return the first value with an earlier occurrence in ``items``.

    Scans ``items`` left-to-right and returns the first element whose
    second occurrence is encountered, or ``None`` if there are no
    duplicates.
    """
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None
