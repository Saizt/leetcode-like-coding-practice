# Union-Find / Disjoint Set Union

## Problem

Implement a data structure that supports efficient grouping of elements into disjoint sets.

The structure should support:

- `find(x)`: return the representative/root of the set containing `x`.
- `union(x, y)`: merge the sets containing `x` and `y`.
- `connected(x, y)`: return whether `x` and `y` belong to the same set.

Union-Find is commonly used for graph connectivity problems.

## Example

```python
uf = UnionFind(5)

uf.union(0, 1)
uf.union(1, 2)

uf.connected(0, 2)  # True
uf.connected(0, 4)  # False

uf.union(3, 4)
uf.union(2, 4)

uf.connected(0, 3)  # True
```

## Core Idea

Each element initially belongs to its own component.

```text
0   1   2   3   4
```

After:

```python
union(0, 1)
union(1, 2)
```

we have:

```text
{0, 1, 2}   {3}   {4}
```

The data structure stores a `parent` array.

```python
parent[x]
```

points to the parent of `x`.

If:

```python
parent[x] == x
```

then `x` is the root representative of its component.

## Invariant

Each connected component is represented as a tree.

The root of each tree is the representative of that component.

Two nodes are connected if and only if they have the same root:

```python
find(x) == find(y)
```

## Path Compression

Without optimization, trees can become tall.

Path compression makes `find` faster by making each visited node point directly to the root.

Before path compression:

```text
0 -> 1 -> 2 -> 3
```

After calling:

```python
find(0)
```

the structure becomes closer to:

```text
0 -> 3
1 -> 3
2 -> 3
3 -> 3
```

This makes future calls faster.

## Union by Rank

When merging two components, we attach the smaller or shallower tree under the deeper tree.

The `rank` array approximates tree depth.

If two trees have the same rank, we choose one root as the new root and increase its rank.

This prevents the tree from becoming unnecessarily tall.

## Complexity

With both path compression and union by rank:

- `find`: almost `O(1)` amortized
- `union`: almost `O(1)` amortized
- `connected`: almost `O(1)` amortized
- Space: `O(n)`

More precisely, the amortized complexity is:

```text
O(alpha(n))
```

where `alpha` is the inverse Ackermann function, which is effectively constant for practical input sizes.

## Edge Cases

Important cases to test:

- union of two separate nodes
- union of already connected nodes
- checking connectivity before and after union
- merging two larger components
- single-element Union-Find
- tracking number of components