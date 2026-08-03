"""Issue 12: find the first duplicate value in a list.

``find_first_duplicate`` scans the input left to right and returns the
first value that already appeared at an earlier index, or ``None`` when
no value repeats. Example: ``[1, 2, 3, 2, 1] -> 2`` (the second ``2``
is the earliest element with a prior occurrence, so it wins over the
later repeated ``1``).
"""

from typing import Any


def find_first_duplicate(items: list) -> Any | None:
    """Return the first element of ``items`` with an earlier occurrence.

    The scan is left to right: the returned value is the earliest element
    whose value was already seen before it. If no element repeats, returns
    ``None`` (including for an empty list).

    Elements must be hashable; unhashable elements raise ``TypeError``.
    Runs in O(n) time and O(n) space.
    """
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None
