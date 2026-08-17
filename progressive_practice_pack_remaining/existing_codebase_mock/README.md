# Existing Codebase Mock — Five-Part Debugging / Extension Practice

This exercise is intentionally different from a clean-room LeetCode problem.

You are given an existing codebase with several abstractions. Your goal is to read only as much of the codebase as necessary, understand the public contracts, and make the tests pass.

Do not assume that every implementation detail is relevant.

---

# Part 1 — Batch Statistics

The service accepts batches of floating-point scores.

Implement/fix the statistics pipeline so that:

- NaN values are ignored when computing per-row minimum, maximum, and sum.
- If a row contains only NaN values, its minimum, maximum, and sum should all be NaN.
- The returned result type must remain unchanged.

---

# Part 2 — Bucketization

The service maps non-negative integer token IDs into a fixed number of buckets.

Implement/fix bucketization so that:

- each token ID contributes one count to `token_id % num_buckets`
- results are returned as a NumPy array of length `num_buckets`
- empty input returns all zeros
- negative token IDs are invalid and must raise `ValueError`

---

# Part 3 — Masked Normalization

Implement/fix masked row normalization.

For each row:

- positions where `mask` is `False` must be returned as NaN
- positions where `mask` is `True` are divided by the sum of all valid, non-NaN values in that row
- NaN values remain NaN
- if the valid non-NaN values in a row sum to zero, all valid positions in that row must become NaN

The implementation should rely on NumPy broadcasting rather than Python loops over individual elements.

---

# Part 4 — Recursive Request Expansion

Requests may contain nested child requests.

Implement/fix recursive expansion so that:

- every leaf request is returned exactly once
- leaves are returned in depth-first, left-to-right order
- a request with no children is a leaf
- recursion depth is not specified; use recursion as needed

---

# Part 5 — Deterministic Sampling

Implement/fix deterministic categorical sampling.

Given a 2D probability array:

- each row represents a categorical distribution
- each row must be sampled independently
- sampling must use `np.random.RandomState(seed)`
- identical input and seed must produce identical output
- rows containing NaN probabilities are invalid and must raise `ValueError`
- rows whose probabilities do not sum to a positive value are invalid and must raise `ValueError`
- probabilities should be normalized per row before sampling

Do not change the public result type.
