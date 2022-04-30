class Solution:

    def longestWord(self, words: List[str]) -> str:
        words.sort()

        vocabulary = {}

        def add(word):
            working = vocabulary
            for index in range(len(word)):
                letter = word[index]
                # print("letter {} with index {}".format(letter, index))
                if letter not in working and index != len(word) - 1:
                    # print("CAUGHT SOMETHING NOT USABLE")
                    return ""
                if letter not in working:
                    working[letter] = {}
                working = working[letter]
            return word

        answer = ""
        for word in words:
            best = add(word)
            if len(best) > len(answer):
                answer = best
            elif len(best) == len(answer) and best < answer:
                answer = best

        return answer