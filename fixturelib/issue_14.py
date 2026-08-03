"""Human-readable byte formatting (issue 14).

Provides :func:`human_bytes`, which renders a byte count using 1024-based
binary units (B, KiB, MiB, ...) and trims a trailing ``.0`` from whole
values, e.g. ``1536 -> "1.5 KiB"`` and ``1048576 -> "1 MiB"``.
"""


def human_bytes(n) -> str:
    """Format a byte count as a human-readable string using 1024-based units.

    Whole values are rendered without a decimal part (``"1 MiB"``); other
    values are rounded to two decimal places with trailing zeros stripped
    (``"1.5 KiB"``).
    """
    units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB"]
    value = float(n)
    index = 0
    while abs(value) >= 1024 and index < len(units) - 1:
        value /= 1024
        index += 1
    if value == int(value):
        text = str(int(value))
    else:
        text = f"{value:.2f}".rstrip("0").rstrip(".")
    return f"{text} {units[index]}"
