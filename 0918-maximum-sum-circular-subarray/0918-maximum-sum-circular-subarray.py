class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        two ways either the maximum is in the normal range
        
        or the maximum is in the circular part
        """
        final_maxim = -float("inf")
        final_minim = float("inf")
        maxim = -float("inf")
        minim = float("inf")
        
        for num in nums:
            maxim = max(maxim + num, num)
            minim = min(minim + num, num)
            
            final_maxim = max(final_maxim, maxim)
            final_minim = min(final_minim, minim)
        
        return max(final_maxim, sum(nums) - final_minim) if final_maxim > 0 else final_maxim