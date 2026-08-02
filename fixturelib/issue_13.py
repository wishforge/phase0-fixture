"""Convert snake_case identifiers to lowerCamelCase (Task 13 / AC-1)."""


def to_camel_case(snake: str) -> str:
    """Return the lowerCamelCase form of a snake_case string.

    Examples:
        >>> to_camel_case("user_id")
        'userId'
        >>> to_camel_case("already_camel_case")
        'alreadyCamelCase'
    """
    parts = [part for part in snake.split("_") if part]
    if not parts:
        return ""
    return parts[0].lower() + "".join(part.capitalize() for part in parts[1:])
