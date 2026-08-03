"""Issue 07: chunked — split a sequence into fixed-size chunks."""


def chunked(seq, n):
    """Split ``seq`` into sublists of at most ``n`` items.

    The final chunk contains the remainder if it is shorter than ``n``.

    Raises:
        ValueError: if ``n`` is not a positive integer.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("chunk size must be a positive integer")
    return [seq[i:i + n] for i in range(0, len(seq), n)]
