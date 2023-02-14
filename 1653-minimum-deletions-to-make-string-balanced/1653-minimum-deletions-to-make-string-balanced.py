class Solution:
    def minimumDeletions(self, s: str) -> int:
        right = s.count("b")
        left = 0
        maxim = right
        
        for idx in range(len(s)):
            char = s[idx]
            left += int(char == "a")
            right -= int(char == "b")
            
            maxim = max(maxim, left + right)
            
        return len(s) - maxim