class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for idx, char in enumerate(word):
            if char == ch:
                return word[:idx + 1][::-1] + word[idx + 1:]
        return word