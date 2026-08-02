"""Task 05 — word_count.

Count case-insensitive word frequencies in a string, splitting on runs of
non-alphanumeric characters. Standard library only.
"""

import re
from collections import Counter


def word_count(text: str) -> dict:
    """Return a dict mapping each lowercased word to its occurrence count.

    Words are extracted by lowercasing ``text`` and splitting on runs of
    non-alphanumeric characters, so punctuation and whitespace are ignored.
    An empty (or whitespace/punctuation-only) string yields an empty dict.
    """
    words = re.findall(r"[a-z0-9]+", text.lower())
    return dict(Counter(words))
