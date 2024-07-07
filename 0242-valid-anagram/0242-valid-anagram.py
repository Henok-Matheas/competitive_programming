class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        
        """
        if len(s) != len(t):
            return False
        
        s_count = [0] * 26
        t_count = [0] * 26
        a_val = ord('a')
        
        
        for idx in range(len(s)):
            s_val = ord(s[idx]) - a_val
            t_val = ord(t[idx]) - a_val
            
            s_count[s_val] += 1
            t_count[t_val] += 1
            
        for idx in range(26):
            if s_count[idx] != t_count[idx]:
                return False
        
        return True