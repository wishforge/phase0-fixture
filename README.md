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

## Delivery smoke 2026-09-14

- 这行改动由 WishForge 自动完成；
- 验证命令 `python -m pytest tests -q` 的真实输出：`20 passed in 0.05s`；
- UTC 时间戳：2026-09-13T18:52:05Z。
