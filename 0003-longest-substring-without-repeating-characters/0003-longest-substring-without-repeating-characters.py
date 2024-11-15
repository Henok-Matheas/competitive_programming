class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        a while loop for the left
        
        have a for while
        the for is just a decoy
        we will also store invalid_char
        
        while left and right less than length
        while right char is not in dict
        right += 1
        
        maxim = 
        
        while right and left char != right char
        count -= 1
        """
        chars = set()
        left = 0
        maxim = 0
        
        for char in s:
            while char in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(char)
            maxim = max(maxim, len(chars))
            
        return maxim
            
        