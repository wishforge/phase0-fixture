# Phase 0 Fixture

Deterministic, independent, verifiable tasks for the WishForge Phase 0 CubeSandbox pilot.
Each `fixturelib/issue_NN.py` is implemented by exactly one task; the matching test in
`tests/` skips itself until that module exists, so the base suite is always green and no
task interferes with another.

Run locally: `python3 -m unittest discover -s tests -v`

- Merge queue smoke test (2026-08-03)
- Merge queue smoke test 2 (2026-08-03)
