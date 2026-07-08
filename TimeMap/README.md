# Time-Based Key-Value Store

## Problem

Design a time-based key-value store that supports two operations:

- `set(key, value, timestamp)`: store the value for `key` at the given `timestamp`.
- `get(key, timestamp)`: return the value associated with `key` at the largest timestamp less than or equal to the given `timestamp`.

If there is no value for the key at or before the requested timestamp, return an empty string `""`.

## Example

```python
tm = TimeMap()

tm.set("foo", "bar", 1)

tm.get("foo", 1)  # "bar"
tm.get("foo", 3)  # "bar"

tm.set("foo", "bar2", 4)

tm.get("foo", 4)  # "bar2"
tm.get("foo", 5)  # "bar2"
tm.get("foo", 0)  # ""
```

## Approach

Use a hash map from each key to a list of `(timestamp, value)` pairs.

```python
{
    "foo": [(1, "bar"), (4, "bar2")]
}
```

For `set`, append the new `(timestamp, value)` pair to the list for that key.

For `get`, perform binary search over that key's timestamp list to find the rightmost timestamp less than or equal to the requested timestamp.

This works efficiently because timestamps are assumed to be inserted in increasing order for each key.

## Invariant

For each key, the list of `(timestamp, value)` pairs is sorted by timestamp in increasing order.

Example:

```text
"foo": [(1, "bar"), (4, "bar2"), (10, "bar3")]
```

So for:

```python
get("foo", 5)
```

we need the rightmost timestamp `<= 5`, which is timestamp `4`.

Therefore, the answer is:

```python
"bar2"
```

## Binary Search Logic

We search for the rightmost timestamp less than or equal to the target timestamp.

If:

```python
mid_time <= timestamp
```

then `mid_value` is a valid candidate, but there may be a later valid timestamp to the right. So we save the current value and move right.

If:

```python
mid_time > timestamp
```

then the current timestamp is too large, so we move left.

At the end, the saved result is the value corresponding to the best timestamp found.

## Complexity

Let `n` be the number of values stored for a particular key.

- `set`: `O(1)`
- `get`: `O(log n)`
- Space: `O(total number of set calls)`

## Edge Cases

Important cases to test:

- getting a key that does not exist
- getting a timestamp before the first stored timestamp
- getting exactly at a stored timestamp
- getting between two stored timestamps
- getting after the latest stored timestamp
- multiple keys
- one key with many timestamped values

## Assumption

This implementation assumes that timestamps passed to `set` are increasing for each key.

If timestamps are not guaranteed to be increasing, then appending is not enough. We would need to keep the list sorted, which may make `set` more expensive.