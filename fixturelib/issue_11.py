"""Capitalize the first letter of each sentence in a string."""


def capitalize_sentences(text: str) -> str:
    """Return *text* with the first letter of every sentence upper-cased.

    A new sentence begins after any of the terminators ``.``, ``!``, or ``?``.
    The very first character of the string is also capitalised.
    """
    if not text:
        return text

    terminators = {".", "!", "?"}
    result: list[str] = []
    capitalize_next = True

    for ch in text:
        if capitalize_next and ch.isalpha():
            result.append(ch.upper())
            capitalize_next = False
        else:
            result.append(ch)

        if ch in terminators:
            capitalize_next = True

    return "".join(result)
