"""Issue 15: basic email validity check (AC-1)."""

import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(address: str) -> bool:
    """Return True if *address* looks like a valid email address.

    Rules (AC-1):
      - exactly one '@'
      - non-empty local part with no whitespace
      - domain containing at least one '.' with non-empty labels
    """
    if not isinstance(address, str):
        return False
    return _EMAIL_RE.fullmatch(address) is not None
