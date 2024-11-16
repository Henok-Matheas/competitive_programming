class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        this is basically the longest repeating character question since and is basically saying we can't have the same values at the same place
        
        
        total will store the bitwise or this is to show which indexes have values stored at them
        
        we will remove while the and of total curr is not zero
        
        total is ored with curren num
        """
        left, total, maxim = 0, 0, 1
        
        
        for right, num in enumerate(nums):
            while total & num:
                total ^= nums[left]
                left += 1
            total |= num
            maxim = max(maxim, right - left + 1)
        
        return maxim