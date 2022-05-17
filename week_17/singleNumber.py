class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        for index in range(1, len(nums)):
            nums[0] ^= nums[index]
        return nums[0]