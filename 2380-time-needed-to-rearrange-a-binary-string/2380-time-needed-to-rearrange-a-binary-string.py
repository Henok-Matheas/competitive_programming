class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        change = True
        count = 0
        s = list(s)
        while change:
            change = False
            idx = 0
            
            while idx < len(s) - 1:
                if s[idx] == "0" and s[idx + 1] == "1":
                    s[idx], s[idx + 1] = s[idx + 1], s[idx]
                    idx += 1
                    change = True
                    
                idx += 1
                    
            count += int(change)
            
        return count