class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()

        i = 0
        j = 0

        max_ = -float("inf")
        while i < len(s):
            while j < len(s) and s[j] not in visited:
                visited.add(s[j])
                j += 1
            max_ = max(max_, j - i)
            visited.remove(s[i])
            i += 1
        return max_ if max_ != -float("inf") else 0