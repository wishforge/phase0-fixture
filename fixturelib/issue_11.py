"""Issue 11: capitalize the first letter of each sentence."""

import re

_SENTENCE_START = re.compile(r"(^|[.!?]\s*)([a-z])")


def capitalize_sentences(text: str) -> str:
    """Return *text* with the first letter of each sentence capitalized.

    A sentence starts at the beginning of the string or after a
    sentence-ending punctuation mark (``.``, ``!``, or ``?``). All other
    characters, including whitespace and existing capitalization, are
    left unchanged.
    """
    return _SENTENCE_START.sub(lambda m: m.group(1) + m.group(2).upper(), text)
