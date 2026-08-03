"""Task 01: format_duration — human-readable duration formatting."""


def format_duration(seconds: int) -> str:
    """Format a non-negative duration in seconds as a compact string.

    - Under a minute:  "Ns"            (e.g. "59s")
    - Under an hour:   "Mm SSs"        (e.g. "2m 05s")
    - One hour or more: "Hh MMm SSs"   (e.g. "1h 05m 30s")
    """
    seconds = int(seconds)
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)

    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    if minutes:
        return f"{minutes}m {secs:02d}s"
    return f"{secs}s"
