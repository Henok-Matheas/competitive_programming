class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxim = 0
        opening = []
        ending = [idx for idx in range(len(s))]
        
        for idx in range(len(s)):
            char = s[idx]
            
            if char == "(":
                opening.append(idx)
                
            elif opening:
                prev = opening.pop()
                ending[prev] = idx + 1
                
        i, j = 0, 0
        
        while j < len(s):
            while j < len(s) and j != ending[j]:
                j = ending[j]
                
            maxim = max(j - i, maxim)
            j += 1
            i = j
            
        return maxim
        