"""Issue 09: parse_semver — parse a strict MAJOR.MINOR.PATCH semantic version."""


def parse_semver(version: str) -> tuple[int, int, int]:
    """Parse a semantic version string of the form "MAJOR.MINOR.PATCH".

    Returns a (major, minor, patch) tuple of ints.
    Raises ValueError if the string does not match exactly.
    """
    if not isinstance(version, str):
        raise ValueError(f"version must be a str, got {type(version).__name__}")

    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError(
            f"invalid semantic version {version!r}: expected exactly 3 dot-separated parts"
        )

    nums = []
    for part in parts:
        if not part.isdigit():
            raise ValueError(
                f"invalid semantic version {version!r}: "
                f"component {part!r} is not a non-negative integer"
            )
        nums.append(int(part))

    return tuple(nums)
