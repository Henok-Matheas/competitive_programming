class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        this is a basic for while
        the while will remove from the left
        
        when do we remove if curr_s != curr_t and maxCost - curr_s - curr_t < 0
        """
        left, maxim = 0, 0
        
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            while maxCost - cost < 0 and left < right:
                left_cost = abs(ord(s[left]) - ord(t[left]))
                maxCost += left_cost
                left += 1
            
            maxCost -= cost
            if maxCost >= 0:
                maxim = max(maxim, right - left + 1)
                
        return maxim
                