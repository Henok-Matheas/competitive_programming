class Solution:

    def minimumLengthEncoding(self, words: List[str]) -> int:
        suffix_trie = {"#": False}

        def add(index, word):
            current = suffix_trie
            for indx in range(len(word) - 1, -1, -1):
                letter = word[indx]
                if letter not in current:
                    current[letter] = {"#": False, "P": index}
                current = current[letter]
                current["P"] = index if len(
                    words[current["P"]]) < len(word) else current["P"]
            current["#"] = True

        for index, word in enumerate(words):
            add(index, word)

        def search(index, word):
            current = suffix_trie
            for indx in range(len(word) - 1, -1, -1):
                letter = word[indx]
                current = current[letter]
            return current["P"]

        count = 0
        size = 0
        for index, word in enumerate(words):
            returned = search(index, word)
            if returned == index:
                count += 1
                size += len(word)
        return size + count
