from collections import Counter


def most_common_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most common whitespace-separated words as (word, count) tuples.

    Words are ordered by count descending; ties preserve first-seen order.
    """
    return Counter(text.split()).most_common(n)
