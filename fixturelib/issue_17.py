"""Issue 17: run-length encoding (standard library only)."""


def run_length_encode(text: str) -> str:
    """Return the run-length encoding of ``text``.

    Each maximal run of equal consecutive characters is encoded as the
    character followed by its run count (e.g. ``"aaabbc" -> "a3b2c1"``).
    An empty string yields an empty string.
    """
    if not text:
        return ""

    parts = []
    prev = text[0]
    count = 1
    for ch in text[1:]:
        if ch == prev:
            count += 1
        else:
            parts.append(f"{prev}{count}")
            prev = ch
            count = 1
    parts.append(f"{prev}{count}")
    return "".join(parts)
