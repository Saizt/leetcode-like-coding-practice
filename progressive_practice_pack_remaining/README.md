# Remaining Progressive Practice Pack

This pack contains the remaining exercises from the original practice plan.

## 1. In-Memory Database

A four-level progressive implementation problem.

Files:
- `in_memory_database/README.md`
- `in_memory_database/database.py`
- `in_memory_database/tests/test_level1.py`
- `in_memory_database/tests/test_level2.py`
- `in_memory_database/tests/test_level3.py`
- `in_memory_database/tests/test_level4.py`

Run from inside `in_memory_database/`:

```bash
python -m unittest tests.test_level1 -v
python -m unittest discover -s tests -p 'test_*.py' -v
```

## 2. Existing Codebase Mock

A five-part debugging / code-reading exercise with intentionally buggy starter files.

Files:
- `existing_codebase_mock/README.md`
- `models.py`
- `stats.py`
- `buckets.py`
- `normalize.py`
- `requests.py`
- `sampling.py`
- tests for Parts 1–5

Run from inside `existing_codebase_mock/`:

```bash
python -m unittest tests.test_part1 -v
python -m unittest discover -s tests -p 'test_*.py' -v
```

For realistic practice, do not read all implementation files first. Start from the README, run the tests, follow failures, and inspect only the relevant parts of the codebase.
