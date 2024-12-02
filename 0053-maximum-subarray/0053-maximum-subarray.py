class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        [0, -2, -1, -4, 0, -1, 1, 2, -7, -3]
        
        
        for every index we just want to know the lowest left we have
        """
        maxim = min(nums)
        p_sum = 0
        low = 0
        
        for num in nums:
            p_sum += num
            maxim = max(maxim, p_sum - low)
            low = min(low, p_sum)
        return maxim
        