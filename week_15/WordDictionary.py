class WordDictionary:

    def __init__(self):
        self.current = {"END": False}

    def addWord(self, word: str) -> None:
        working = self.current
        for letter in word:
            if letter not in working:
                working[letter] = {"END": False}
            working = working[letter]
        working["END"] = True

    def search(self, word: str) -> bool:
        workings = [self.current]
        for letter in word:
            secondary = []
            if letter == ".":
                while workings:
                    working = workings.pop()
                    for ltr in working:
                        if ltr != "END":
                            secondary.append(working[ltr])
            while workings:
                working = workings.pop()
                if letter in working:
                    secondary.append(working[letter])
            if not secondary:
                return False
            workings = secondary

        for working in workings:
            if working["END"]:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)