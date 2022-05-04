class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        vocabulary = {"END": False, "COUNT": 0}

        last_index = defaultdict(int)

        for index in range(len(words)):
            word = words[index]
            last_index[word] = index

        answer = []
        for index in range(len(words)):
            word = words[index]
            word_count[word] -= 1
            if index == last_index[word]:
                heapq.heappush(answer, [word_count[word], word])

        final = [heapq.heappop(answer)[1] for i in range(k)]
        return final

        # heap implementation
        vocabulary = {"END": False, "COUNT": 0}

        last_index = defaultdict(int)

        for index in range(len(words)):
            word = words[index]
            last_index[word] = index

        answer = []

        def add(index, word):
            current = vocabulary
            for letter in word:
                if letter not in current:
                    current[letter] = {"END": False, "END": False, "COUNT": 0}
                current = current[letter]
                current["COUNT"] -= 1
            current["END"] = True

            if index == last_index[word]:
                heapq.heappush(answer, [current["COUNT"], word])

        answer = []
        for index in range(len(words)):
            word = words[index]
            add(index, word)

        final = [heapq.heappop(answer)[1] for i in range(k)]
        return final
