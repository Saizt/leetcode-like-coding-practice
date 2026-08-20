# Signal Garden — Debugging Mock 1

You are given an existing Python codebase with failing unit tests.

Your task is to identify and fix the root causes so that as many tests as possible pass.

## Rules

- Do not redesign the entire project.
- Prefer minimal fixes that preserve the existing architecture.
- The test suite is the final word on intended behavior.
- You may inspect any source file or test.
- You may use `print`, `breakpoint()`, `pdb`, and Python/NumPy documentation.
- Assume no hidden requirements beyond what is exercised by the tests.

## Running tests

From this directory:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Run one module:

```bash
python -m unittest tests.test_pipeline -v
```

Run one test:

```bash
python -m unittest tests.test_pipeline.PipelineTests.test_masked_rows_are_ignored -v
```

## Context

The package implements a small "signal garden" pipeline.

A collection of observations is converted into a recursive region tree. Leaf observations are featurized, normalized, assigned to integer bins, and summarized into a report.

You do not need domain knowledge. Read only as much of the codebase as necessary to understand failing behavior.
