class UnionFind:

    def __init__(self, n: int):
        self.parent = list(range(n))
        # self.rank = [0] * n #rank
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[x]

        return x
    # path compression
    #     if self.parent[x] != x:
    #         self.parent[x] = self.find(self.parent[x])

    #     return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_x] = root_y
        # # Union by rank: attach shallower tree under deeper tree.
        # if self.rank[root_x] < self.rank[root_y]:
        #     self.parent[root_x] = root_y
        # elif self.rank[root_x] > self.rank[root_y]:
        #     self.parent[root_y] = root_x
        # else:
        #     self.parent[root_y] = root_x
        #     self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    # Basic initialization
    uf = UnionFind(5)

    assert uf.components == 5
    assert uf.connected(0, 1) is False
    assert uf.connected(3, 4) is False

    # Union some nodes
    assert uf.union(0, 1) is True
    assert uf.connected(0, 1) is True
    assert uf.components == 4

    assert uf.union(1, 2) is True
    assert uf.connected(0, 2) is True
    assert uf.connected(2, 1) is True
    assert uf.components == 3

    # Separate component
    assert uf.union(3, 4) is True
    assert uf.connected(3, 4) is True
    assert uf.connected(0, 4) is False
    assert uf.components == 2

    # Merge two larger components
    assert uf.union(2, 4) is True
    assert uf.connected(0, 3) is True
    assert uf.connected(1, 4) is True
    assert uf.components == 1

    # Union already connected nodes should return False
    assert uf.union(0, 4) is False
    assert uf.components == 1

    # Single-element structure
    uf = UnionFind(1)
    assert uf.connected(0, 0) is True
    assert uf.union(0, 0) is False
    assert uf.components == 1

    print("All tests passed.")