# LRU Cache

## Problem

Design a data structure that supports the following operations:

- `get(key)`: return the value associated with `key` if it exists, otherwise return `-1`.
- `put(key, value)`: insert or update the value for `key`.

The cache has a fixed capacity. If inserting a new key exceeds the capacity, the least recently used key should be evicted.

Both `get` and `put` should run in `O(1)` time.

## Solution

Use two data structures:

1. A hash map: `key -> node`
2. A doubly linked list ordered from least recently used to most recently used

The hash map gives constant-time access to nodes.  
The doubly linked list gives constant-time removal and insertion.

The least recently used item is stored right after the dummy `head`.  
The most recently used item is stored right before the dummy `tail`.

## Invariant

The linked list is always ordered as:

```text
head <-> least recently used <-> ... <-> most recently used <-> tail