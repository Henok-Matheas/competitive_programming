class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            if i < len(nums):
                nums[j] = nums[i]
                j += 1
            i += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
