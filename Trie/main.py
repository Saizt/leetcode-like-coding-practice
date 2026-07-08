class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children.keys():
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_word = True

    def _find_node(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children.keys():
                return None
            else:
                curr = curr.children[char]

        return curr

    def search(self, word):
        curr = self._find_node(word)
        return curr is not None and curr.is_word
            
    def startsWith(self, prefix):
        curr = self._find_node(prefix)

        return curr is not None


if __name__ == "__main__":
    trie = Trie()

    # Empty trie
    assert trie.search("apple") is False
    assert trie.startsWith("app") is False

    # Insert one word
    trie.insert("apple")

    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True

    # Insert prefix as a word
    trie.insert("app")

    assert trie.search("app") is True
    assert trie.search("apple") is True
    assert trie.startsWith("ap") is True
    assert trie.startsWith("apple") is True
    assert trie.startsWith("banana") is False

    # Insert another branch
    trie.insert("bat")
    trie.insert("bath")
    trie.insert("bad")

    assert trie.search("bat") is True
    assert trie.search("bath") is True
    assert trie.search("bad") is True
    assert trie.search("ba") is False
    assert trie.startsWith("ba") is True
    assert trie.startsWith("bat") is True
    assert trie.startsWith("bath") is True
    assert trie.startsWith("bad") is True
    assert trie.startsWith("cat") is False

    # Duplicate insert should not break anything
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.startsWith("app") is True

    print("All tests passed.")