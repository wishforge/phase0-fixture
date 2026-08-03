"""Task 03 — palindrome check (standard library only)."""


def is_palindrome(s: str) -> bool:
    """Return True if *s* is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]
