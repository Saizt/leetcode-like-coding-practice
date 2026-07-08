class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.getMin()))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            pass

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    # Basic test
    s = MinStack()
    assert s.getMin() == None
    assert s.top() == None
    s.pop() 

    s.push(5)
    s.push(3)
    s.push(7)

    assert s.getMin() == 3
    assert s.top() == 7

    s.pop()
    assert s.top() == 3
    assert s.getMin() == 3

    s.pop()
    assert s.top() == 5
    assert s.getMin() == 5

    # Duplicate minimum test
    s = MinStack()
    s.push(2)
    s.push(2)
    s.push(3)

    assert s.getMin() == 2

    s.pop()
    assert s.getMin() == 2

    s.pop()
    assert s.getMin() == 2
    assert s.top() == 2

    # Negative numbers test
    s = MinStack()
    s.push(-1)
    s.push(-3)
    s.push(0)

    assert s.getMin() == -3
    assert s.top() == 0

    s.pop()
    assert s.getMin() == -3
    assert s.top() == -3

    s.pop()
    assert s.getMin() == -1
    assert s.top() == -1

    # sequence
    s = MinStack()
    s.push(4)
    s.push(1)
    s.push(1)
    s.push(3)

    assert s.getMin() == 1

    s.pop()
    assert s.getMin() == 1

    s.pop()
    assert s.getMin() == 1

    s.pop()
    assert s.getMin() == 4

    print("All tests passed.")