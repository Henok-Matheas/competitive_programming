class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        current = -float("inf")
        indx = 0
        for idx in range(len(nums)):
            if nums[idx] != current:
                current = nums[idx]
                nums[indx] = nums[idx]
                indx += 1
            else:
                nums[idx] = float("inf")
        return indx