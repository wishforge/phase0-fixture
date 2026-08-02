"""Task 16: recursive dictionary merging."""


def deep_merge(base, override):
    """Recursively merge ``override`` into ``base``.

    Returns a new dict. For keys present in both inputs where both values
    are dicts, the values are merged recursively; otherwise ``override``
    wins. Neither input is mutated.
    """
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
