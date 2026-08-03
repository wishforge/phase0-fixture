"""Task 17: run-length encoding (AC-1)."""


def run_length_encode(text: str) -> str:
    """Encode runs of identical characters as <char><run-length>.

    Examples: "aaabbc" -> "a3b2c1", "" -> "", "a" -> "a1".
    """
    parts = []
    prev = None
    count = 0
    for ch in text:
        if ch == prev:
            count += 1
        else:
            if count:
                parts.append(prev + str(count))
            prev = ch
            count = 1
    if count:
        parts.append(prev + str(count))
    return "".join(parts)
