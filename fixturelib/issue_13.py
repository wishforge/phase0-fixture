"""Task 13: Convert snake_case identifiers to camelCase."""


def to_camel_case(snake_case: str) -> str:
    """Convert a snake_case string to camelCase."""
    parts = snake_case.split("_")
    return parts[0].lower() + "".join(word.capitalize() for word in parts[1:])
