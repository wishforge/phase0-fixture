def parse_semver(version: str) -> tuple[int, int, int]:
    """Parse a 'MAJOR.MINOR.PATCH' string into a tuple of three ints.

    Raises ValueError if the string is not exactly three dot-separated
    non-negative integer components.
    """
    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError(f"invalid semver: {version!r}")
    nums = []
    for part in parts:
        if not part.isdigit():
            raise ValueError(f"invalid semver component: {part!r}")
        nums.append(int(part))
    return (nums[0], nums[1], nums[2])
