"""Self-contained CSV line parser for issue 02.

Standard-library-only implementation that parses a single CSV record into a
list of field strings, supporting quoted fields and escaped quotes.
"""

from __future__ import annotations


def parse_csv_line(line: str) -> list[str]:
    """Parse a single CSV record into a list of field strings.

    Supports quoted fields (commas inside quotes are literal) and escaped
    quotes represented as doubled quote characters ("").
    """
    if line == "":
        return []

    fields: list[str] = []
    buf: list[str] = []
    in_quotes = False
    i = 0
    length = len(line)

    while i < length:
        ch = line[i]
        if in_quotes:
            if ch == '"':
                if i + 1 < length and line[i + 1] == '"':
                    buf.append('"')
                    i += 1
                else:
                    in_quotes = False
            else:
                buf.append(ch)
        else:
            if ch == '"':
                in_quotes = True
            elif ch == ",":
                fields.append("".join(buf))
                buf = []
            else:
                buf.append(ch)
        i += 1

    fields.append("".join(buf))
    return fields
