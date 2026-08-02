"""Issue 08: slugify — convert a string to a URL-friendly slug."""

import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Lowercase *text*, collapse non-alphanumeric runs to '-', and trim edges."""
    return _NON_ALNUM.sub("-", text.lower()).strip("-")
