class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    # Search exact word
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    # Prefix search (startsWith)
    def startsWith(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# ---------------- MAIN ----------------
if __name__ == "__main__":

    trie = Trie()

    # Word set
    words = ["apple", "app", "bat", "ball", "cat"]

    print("Inserting words:")
    for w in words:
        print("Insert:", w)
        trie.insert(w)

    print("\nSearch Operations:")
    print("apple ->", trie.search("apple"))
    print("app ->", trie.search("app"))
    print("appl ->", trie.search("appl"))  # incomplete word

    print("\nPrefix Operations:")
    print("app ->", trie.startsWith("app"))
    print("ba ->", trie.startsWith("ba"))
    print("dog ->", trie.startsWith("dog"))