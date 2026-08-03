"""Task 19: parse_query_string — parse a URL query string into a dict.

Standard-library only; duplicate keys resolve to their first value.
"""
from urllib.parse import unquote_plus


def parse_query_string(query: str) -> dict:
    """Parse ``query`` into a dict of string keys to string values.

    - Percent-encoded sequences (and ``+``) are decoded.
    - On duplicate keys, the first value wins.
    - Empty/whitespace-only input yields {}.
    - Pairs without ``=`` map to an empty string.
    - A leading ``?`` is tolerated.
    """
    result = {}
    if query is None:
        return result
    query = query.lstrip("?")
    for pair in query.split("&"):
        if not pair:
            continue
        key, sep, value = pair.partition("=")
        key = unquote_plus(key)
        if key not in result:
            result[key] = unquote_plus(value)
    return result
