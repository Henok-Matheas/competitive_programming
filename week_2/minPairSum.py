class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxim = nums[0] + nums[-1]
        
        for i in range(len(nums) // 2):
            value = nums[i] + nums[-(i + 1)]
            if value > maxim:
                maxim = value
        return maxim