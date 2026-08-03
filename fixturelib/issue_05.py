"""Issue 05: word_count — count word occurrences in a string."""

import re


def word_count(text: str) -> dict[str, int]:
    """Return case-insensitive word counts for ``text``.

    Words are runs of alphanumeric characters; everything else
    (punctuation, whitespace) acts as a separator. Empty input
    yields ``{}``.
    """
    counts: dict[str, int] = {}
    for word in re.findall(r"[a-zA-Z0-9]+", text.lower()):
        counts[word] = counts.get(word, 0) + 1
    return counts
