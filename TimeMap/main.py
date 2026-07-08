from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key, value, timestamp):
        self.storage[key].append((timestamp, value))

    def get(self, key, timestamp):
        res = ""
        if key in self.storage.keys():
            items = self.storage[key]

            l, r = 0, len(items)-1
            while l<=r:
                mid = (l+r)//2
                if items[mid][0] <= timestamp:
                    res = items[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            
        return res
    
    
if __name__ == "__main__":
    tm = TimeMap()

    assert tm.get("foo", 1) == ""

    tm.set("foo", "bar", 1)

    assert tm.get("foo", 0) == ""
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

    tm.set("foo", "bar2", 4)

    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    tm.set("baz", "x", 2)

    assert tm.get("baz", 1) == ""
    assert tm.get("baz", 2) == "x"
    assert tm.get("foo", 2) == "bar"

    print("All tests passed.")