"""Convert integers to Roman numerals (Issue 20).

Standard-library-only implementation of ``to_roman`` for 1..3999.
"""

_ROMAN_TABLE = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
)


def to_roman(n: int) -> str:
    """Return the Roman numeral representation of ``n`` for 1 <= n <= 3999.

    Raises ValueError for any value outside that range.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"expected an integer, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"expected an integer in 1..3999, got {n}")

    parts = []
    for value, numeral in _ROMAN_TABLE:
        while n >= value:
            parts.append(numeral)
            n -= value
    return "".join(parts)
