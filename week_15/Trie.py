class Trie:

    def __init__(self):
        self.starting = {"END" : False}
        

    def insert(self, word: str) -> None:
        working = self.starting
        for letter in word:
            if letter not in working:
                working[letter] = {"END" : False}
            working = working[letter]
        working["END"] = True
        
    def search(self, word: str) -> bool:
        working = self.starting
        for letter in word:
            if letter in working:
                working = working[letter]
            else:
                return False
        return working['END']

    def startsWith(self, prefix: str) -> bool:
        working = self.starting
        for letter in prefix:
            if letter not in working:
                return False
            working = working[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)