# WishForge phase0 fixture

Deterministic, independent, verifiable tasks for the WishForge Phase 0 CubeSandbox pilot.
Each `fixturelib/issue_NN.py` is implemented by exactly one task; the matching test in
`tests/` skips itself until that module exists, so the base suite is always green and no
task interferes with another.

## Install

Requires Python 3.12 (the version used by CI); no third-party dependencies.
From the repository root, verify your checkout with:

```bash
python3 -m unittest discover -s tests -v
```

Tasks that are not yet implemented show up as skipped, so the suite is always green.
