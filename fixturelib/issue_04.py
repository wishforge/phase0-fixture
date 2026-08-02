"""Utilities for issue 04: recursively flatten nested lists."""


def flatten(nested):
    """Return a new flat list with all nested lists recursively expanded.

    Non-list items (including strings) are treated as atomic leaves.
    Order is preserved and the input is not mutated. Uses an iterative,
    stack-based traversal so arbitrarily deep nesting is handled without
    hitting recursion limits. Standard library only.
    """
    result = []
    stack = list(reversed(nested))
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(item)
    return result
