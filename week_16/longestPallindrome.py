class Solution:

    def longestPalindrome(self, s: str) -> str:
        max_ = (0, 0)
        for index, num in enumerate(s):
            i, j = index - 1, index + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if j - i - 1 > max_[1] - max_[0] + 1:
                max_ = (i + 1, j - 1)

            i, j = index, index + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if j - i - 1 > max_[1] - max_[0] + 1:
                max_ = (i + 1, j - 1)
        return s[max_[0]:max_[1] + 1]
