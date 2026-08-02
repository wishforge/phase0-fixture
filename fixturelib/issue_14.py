"""Issue 14: human-readable byte sizes (binary units)."""

_UNITS = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")


def human_bytes(n):
    """Return *n* bytes as a human-readable string using binary units.

    Examples: 0 -> "0 B", 1024 -> "1 KiB", 1536 -> "1.5 KiB".
    """
    value = float(n)
    for unit in _UNITS:
        if abs(value) < 1024 or unit == _UNITS[-1]:
            return f"{value:g} {unit}"
        value /= 1024
