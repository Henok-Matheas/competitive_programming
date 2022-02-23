class Node:

    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        lst = []
        for key in dict:
            lst.append(Node(dict[key], key))

        heapq.heapify(lst)
        ordered = heapq.nlargest(k, lst)

        final = []

        for i in ordered:
            final.append(i.word)

        # final.sort()
        return final
