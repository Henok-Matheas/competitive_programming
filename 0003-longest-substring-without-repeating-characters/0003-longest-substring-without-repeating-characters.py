class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        for every val
            have a set and if there is val in set
            empty set
            max =
        """
        max_length = 0
        left = 0
        chars = {}
        
        for idx in range(len(s)):
            char = s[idx]
            
            while char in chars:
                chars.pop(s[left])
                left += 1
            
            chars[char] = idx
            
            max_length = max(max_length, len(chars))
        
        return max_length