class Trie:

    def __init__(self):
        self.trie = {"#": False}

    def insert(self, word: str) -> None:
        current = self.trie
        for char in word:
            if char not in current:
                current[char] = {"#": False}
            current = current[char]
        current["#"] = True

    def search(self, word: str) -> bool:
        current = self.trie
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return current["#"]

    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)