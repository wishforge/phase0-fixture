"""Issue 08: slugify."""

import re


def slugify(title: str) -> str:
    """Lowercase ``title``, replace non-alphanumerics with '-', collapse repeats, trim."""
    title = title.lower()
    title = re.sub(r"\s+", "-", title)
    title = re.sub(r"[^a-z0-9-]+", "", title)
    title = re.sub(r"-{2,}", "-", title)
    return title.strip("-")
