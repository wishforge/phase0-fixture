"""Format a duration in seconds as a human-readable string."""


def format_duration(seconds: int) -> str:
    """Return a compact human-readable duration string.

    Examples:
        >>> format_duration(0)
        '0s'
        >>> format_duration(125)
        '2m 05s'
        >>> format_duration(3930)
        '1h 05m 30s'
    """
    if seconds < 0:
        raise ValueError("seconds must be non-negative")

    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)

    if hours:
        return f"{hours}h {minutes:02d}m {secs:02d}s"
    if minutes:
        return f"{minutes}m {secs:02d}s"
    return f"{secs}s"
