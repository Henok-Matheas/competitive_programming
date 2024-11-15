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
        counter = defaultdict(int)
        maxim = 0
        left, right = 0, 0
        while left < len(s) and right < len(s):
            while right < len(s) and counter[s[right]] == 0:
                counter[s[right]] += 1
                right += 1
            
            maxim = max(maxim, right - left)
            
            while right < len(s) and counter[s[right]]:
                counter[s[left]] -= 1
                left += 1
                
        return maxim
        