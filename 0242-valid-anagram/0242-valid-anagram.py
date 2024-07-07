class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        
        """
        char_count = [0] * (ord("z") - ord("a") + 1)
        
        
        for char in s:
            char_count[ord(char) - ord("a")] += 1
            
        for char in t:
            char_count[ord(char) - ord("a")] -= 1
            
        for count in char_count:
            if count != 0:
                return False
            
        return True
        
        
        for idx in range(len(s)):
            s_val = ord(s[idx]) - a_val
            t_val = ord(t[idx]) - a_val
            
            s_count[s_val] += 1
            t_count[t_val] += 1
            
        for idx in range(26):
            if s_count[idx] != t_count[idx]:
                return False
        
        return True