"""Issue 15 – basic e-mail validation (stdlib only)."""


def is_valid_email(address: str) -> bool:
    """Return True if *address* looks like a valid e-mail address.

    Rules (intentionally simple):
      - exactly one '@'
      - non-empty local part and domain
      - at least one dot in the domain
      - no whitespace anywhere
    """
    if not isinstance(address, str):
        return False
    if any(ch.isspace() for ch in address):
        return False
    if address.count("@") != 1:
        return False
    local, domain = address.split("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True
