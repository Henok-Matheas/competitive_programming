class WordFilter:

    def __init__(self, words: List[str]):
        self.prfx = {}
        self.sufx = {}
        self.visited = {}

        def add(index, word):
            currPre = self.prfx
            currSuf = self.sufx
            for indx in range(len(word)):
                prelet = word[indx]
                suflet = word[len(word) - 1 - indx]
                if prelet not in currPre:
                    currPre[prelet] = {"INDEX": set()}

                if suflet not in currSuf:
                    currSuf[suflet] = {"INDEX": set()}

                currPre = currPre[prelet]
                currSuf = currSuf[suflet]

                if word in self.visited:
                    currPre["INDEX"].remove(self.visited[word])
                    currSuf["INDEX"].remove(self.visited[word])
                currPre["INDEX"].add(index)
                currSuf["INDEX"].add(index)

        # words.sort()
        for index, word in enumerate(words):
            add(index, word)
            self.visited[word] = index

        # print("the prefix dict is",self.prfx)
        # print("the suffix dict is",self.sufx)

    def f(self, prefix: str, suffix: str) -> int:

        def search(dicti, word):
            current = dicti
            for letter in word:
                if letter not in current:
                    return []
                current = current[letter]
            return current['INDEX']

        preset = search(self.prfx, prefix)
        sufset = search(self.sufx, suffix[::-1])

        answer = -1
        for index in preset:
            if index in sufset:
                answer = max(answer, index)
        return answer


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)