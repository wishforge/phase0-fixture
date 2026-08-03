"""Issue 04: ``flatten``.

Provides :func:`flatten`, which recursively flattens arbitrarily nested
lists (and tuples) into a single flat list while preserving element order.
Non-sequence items, including strings and bytes, are treated as atomic
leaves. Implemented with an explicit stack so deep nesting does not hit
Python's recursion limit.
"""


def flatten(nested: list) -> list:
    """Return a new list with all nested lists/tuples flattened.

    Example:
        >>> flatten([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    result = []
    stack = [iter(nested)]
    while stack:
        try:
            item = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue
        if isinstance(item, (list, tuple)):
            stack.append(iter(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[1], 2, [3, [4]]]) == [1, 2, 3, 4]
    assert flatten([[[[]]]]) == []
    print("issue_04 self-checks passed")
