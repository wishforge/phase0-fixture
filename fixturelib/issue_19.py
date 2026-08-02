"""Parse a URL query string into a dict (first occurrence wins)."""

from urllib.parse import unquote_plus


def parse_query_string(query: str) -> dict:
    """Split a query string on ``&``/``=`` into a dict.

    Keys and values are percent-decoded (``+`` becomes a space). For
    duplicate keys the first occurrence wins. Blank values are kept.
    """
    result = {}
    if not query:
        return result
    for pair in query.split("&"):
        if not pair:
            continue
        if "=" in pair:
            key, _, value = pair.partition("=")
        else:
            key, value = pair, ""
        key = unquote_plus(key)
        value = unquote_plus(value)
        if key not in result:
            result[key] = value
    return result
