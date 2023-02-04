class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wanted = [0 for _ in range(ord('z') - ord('a') + 1)]
        have = [0 for _ in range(ord('z') - ord('a') + 1)]
        needed = len(s1)
        for char in s1:
            wanted[ord(char) - ord('a')] += 1
        i, j = 0, 0
        while j < len(s2):
            while j < len(s2) and j - i < len(s1):
                if wanted[ord(s2[j]) - ord('a')]:
                    have[ord(s2[j]) - ord('a')] += 1
                    if have[ord(s2[j]) - ord('a')] <= wanted[ord(s2[j]) - ord('a')]:
                        needed -= 1
                j += 1
            if not needed:
                return True
            if wanted[ord(s2[i]) - ord('a')]:
                have[ord(s2[i]) - ord('a')] -= 1
                if have[ord(s2[i]) - ord('a')] < wanted[ord(s2[i]) - ord('a')]:
                    needed += 1
            i += 1
        return False