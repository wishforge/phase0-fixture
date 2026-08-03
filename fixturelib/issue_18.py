"""Task 18: count the most common words in a text."""

from collections import Counter


def most_common_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return up to ``n`` most common whitespace-delimited words.

    The result is a list of ``(word, count)`` tuples sorted by count
    descending and, for equal counts, by word ascending.
    """
    counts = Counter(text.split())
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[: max(n, 0)]
