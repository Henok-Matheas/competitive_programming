class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        current = -float("inf")
        for idx in range(len(nums)):
            if nums[idx] != current:
                current = nums[idx]
            else:
                nums[idx] = float("inf")
        nums.sort()
        count = 0
        for num in nums:
            count += 1 if num != float("inf") else 0
        return count