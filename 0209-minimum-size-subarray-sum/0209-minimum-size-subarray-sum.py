class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        for every idx have a total sum
            while that total sum is less than target
            include neighbours
            
            if total greater or equal have the length
            total - current
        """
        total = 0
        minim = len(nums) + 1
        right = 0
        for idx, curr in enumerate(nums):
            while right < len(nums) and total < target:
                total += nums[right]
                right += 1
            
            if total >= target:
                minim = min(minim, right - idx)
                
            total -= curr
            
        return minim if minim != len(nums) + 1 else 0