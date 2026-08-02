def is_palindrome(text: str) -> bool:
    """Return True if `text` is a palindrome, ignoring case and non-alphanumerics."""
    cleaned = [c.lower() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
