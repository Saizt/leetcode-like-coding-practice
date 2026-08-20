# Phase Lattice — Debugging Mock 2

You are given an unfamiliar Python package with a failing unit test suite.

Your task is to fix the root causes so that as many tests as possible pass.

## Rules
- Preserve the existing public API.
- Prefer minimal fixes over redesigns.
- The tests are the final word on intended behavior.
- Do not assume untested requirements.
- You may use `print`, `breakpoint()`, `pdb`, and Python/NumPy documentation.

## Run
```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Some failures may share a root cause. Fixing one issue may expose another.
