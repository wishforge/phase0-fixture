"""Issue 16: deep_merge."""


def deep_merge(a: dict, b: dict) -> dict:
    """Return a new dict recursively merging ``b`` into ``a``.

    Keys from ``b`` override keys from ``a``; when a key is present in
    both with dict values, the nested dicts are merged the same way.
    Neither input is mutated.
    """
    result = dict(a)
    for key, b_val in b.items():
        if key in result and isinstance(result[key], dict) and isinstance(b_val, dict):
            result[key] = deep_merge(result[key], b_val)
        else:
            result[key] = b_val
    return result
