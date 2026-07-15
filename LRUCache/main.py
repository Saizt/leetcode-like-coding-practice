class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Mark as most recently used
        self._remove(node)
        self._add_to_back(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # Updated key becomes most recently used
            self._remove(node)
            self._add_to_back(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_back(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_back(self, node: Node) -> None:
        last = self.tail.prev

        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        

if __name__=="__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1)==1 # returns 1; key 1 becomes most recent

    cache.put(3, 3) # evicts key 2
    assert cache.get(2)==-1 # returns -1

    cache.put(4, 4) # evicts key 1
    assert cache.get(1)==-1 # returns -1
    assert cache.get(3)==3 # returns 3
    assert cache.get(4)==4 # returns 4
    print('All tests passed.')