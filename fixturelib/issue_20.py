"""Roman numeral conversion for issue 20."""

__all__ = ["to_roman"]

_ROMAN_TABLE = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def to_roman(n: int) -> str:
    """Convert an integer in 1..3999 to its Roman numeral representation.

    Raises ``ValueError`` if ``n`` is not an integer in the supported range.
    """
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 3999:
        raise ValueError("to_roman requires an integer in 1..3999")

    parts = []
    for value, symbol in _ROMAN_TABLE:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)
