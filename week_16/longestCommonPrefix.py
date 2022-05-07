class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        vocabulary = {}
        workng = vocabulary
        for letter in strs[0]:
            if letter not in workng:
                workng[letter] = {}
            workng = workng[letter]

        for index in range(1, len(strs)):
            word = strs[index]
            working = vocabulary
            for letter in word:
                if letter not in working:
                    working.clear()
                    break
                working = working[letter]
            working.clear()
        answer = ""
        working = vocabulary
        while working:
            for letter in working:
                answer += letter
                working = working[letter]
        return answer
