# MinStack

## Problem

Design a stack that supports the following operations:

- `push(val)`: add a value to the stack.
- `pop()`: remove the top value from the stack.
- `top()`: return the top value of the stack.
- `getMin()`: return the minimum value currently in the stack.

All operations should run in `O(1)` time.

## Approach

A normal stack can support `push`, `pop`, and `top` in `O(1)` time.

The challenge is `getMin()`. If we call `min(stack)`, that takes `O(n)` time.

To make `getMin()` constant time, use two stacks:

1. `stack`: stores the actual values.
2. `min_stack`: stores the minimum value at each stack depth.

## Invariant

For every index `i`:

```text
min_stack[i] = minimum value among stack[0:i+1]
```

Therefore, the current minimum is always:

```python
min_stack[-1]
```

## Example

After these operations:

```python
push(5)
push(3)
push(7)
push(2)
```

The internal state is:

```text
stack:     [5, 3, 7, 2]
min_stack: [5, 3, 3, 2]
```

So:

```python
getMin() == 2
```

If we pop once:

```text
stack:     [5, 3, 7]
min_stack: [5, 3, 3]
```

Now:

```python
getMin() == 3
```

## Why This Works

Every time we push a value, we also push the minimum value seen so far.

When we pop from the main stack, we also pop from the minimum stack. This keeps both stacks aligned.

The top of `min_stack` always corresponds to the minimum value in the current stack.

## Complexity

Let `n` be the number of values in the stack.

- `push`: `O(1)`
- `pop`: `O(1)`
- `top`: `O(1)`
- `getMin`: `O(1)`
- Space: `O(n)`

## Edge Cases

Important cases to test:

- duplicate minimum values
- negative values
- popping after the minimum value appears
- one-element stack