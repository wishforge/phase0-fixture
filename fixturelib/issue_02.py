"""AC-1: Parse one CSV line into a list of fields.

Self-contained, standard-library-only implementation. Uses the ``csv``
module so that quoted fields and doubled-quote (``""``) escapes are handled
consistently.
"""
import csv
import io


def parse_csv_line(line: str) -> list[str]:
    """Parse a single CSV line into a list of string fields.

    Quoted fields may contain commas, and doubled quotes (``""``) inside a
    quoted field collapse to a single literal quote. A trailing comma yields
    a trailing empty string. An empty input line yields an empty list.
    """
    if not line:
        return []
    return next(csv.reader(io.StringIO(line)))
