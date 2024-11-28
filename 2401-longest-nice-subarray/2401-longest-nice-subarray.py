class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        while the bitwise and of the total and current is not zero
        do a bitwise xor of the total and left
        
        then do bitwise or of the current and total
        """
        total, maxim = 0, 0
        left = 0
        
        for right, num in enumerate(nums):
            while total & num:
                total ^= nums[left]
                left += 1   
            total |= num
            maxim = max(maxim, right - left + 1)
            
        return maxim
            