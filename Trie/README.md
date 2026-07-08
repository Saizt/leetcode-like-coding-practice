# Trie

## Problem

Design a Trie, also called a prefix tree, that supports the following operations:

- `insert(word)`: insert a word into the trie.
- `search(word)`: return `True` if the full word exists in the trie.
- `startsWith(prefix)`: return `True` if there is any word in the trie that starts with the given prefix.

## Example

```python
trie = Trie()

trie.insert("apple")

trie.search("apple")    # True
trie.search("app")      # False
trie.startsWith("app")  # True

trie.insert("app")

trie.search("app")      # True
```

## Approach

A trie is a tree-like data structure where each node represents a prefix.

Each node contains:

- `children`: a hash map from character to child node
- `is_word`: a boolean indicating whether this node marks the end of a complete inserted word

For example, after inserting `"apple"`:

```text
root
 |
 a
 |
 p
 |
 p
 |
 l
 |
 e  (is_word = True)
```

The prefix `"app"` exists in the trie, but it is not a complete word until we explicitly insert `"app"`.

## Invariant

Each path from the root represents a prefix.

A node with:

```python
is_word = True
```

marks the end of a complete inserted word.

Therefore:

- `startsWith(prefix)` only needs to verify that the prefix path exists.
- `search(word)` must verify that the path exists and that the final node has `is_word = True`.

## Implementation Details

Use a helper method:

```python
_find_node(text)
```

This method walks through the trie following the characters of `text`.

If the path exists, it returns the final node.

If the path does not exist, it returns `None`.

Then:

```python
search(word)
```

returns `True` only if `_find_node(word)` exists and `is_word` is `True`.

```python
startsWith(prefix)
```

returns `True` if `_find_node(prefix)` exists.

## Complexity

Let `L` be the length of the input word or prefix.

- `insert`: `O(L)`
- `search`: `O(L)`
- `startsWith`: `O(L)`

Space:

- `O(total number of characters inserted)`

In the worst case, if no words share prefixes, each character creates a new node.

## Edge Cases

Important cases to test:

- searching in an empty trie
- searching for a prefix that has not been inserted as a full word
- inserting a word and then inserting its prefix
- words that share prefixes
- duplicate inserts
- prefixes that do not exist