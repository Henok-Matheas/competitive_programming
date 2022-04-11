class Solution:

    def rob(self, nums: List[int]) -> int:

        maxim = 0
        bound = lambda row: row >= 0 and row < len(nums)
        for i in range(len(nums)):
            jump2 = nums[i - 2] if bound(i - 2) else 0
            jump3 = nums[i - 3] if bound(i - 3) else 0

            nums[i] += max(jump2, jump3)

            maxim = max(maxim, nums[i])
        return maxim