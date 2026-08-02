def chunked(seq, size):
    """Split *seq* into sub-lists of length *size* (last chunk may be shorter).

    Raises ValueError if size < 1.
    """
    if size < 1:
        raise ValueError("chunk size must be >= 1")
    return [list(seq[i:i + size]) for i in range(0, len(seq), size)]
