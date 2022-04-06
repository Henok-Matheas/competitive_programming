class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        for idx in range(len(nums)):
            if leftsum == rightsum - nums[idx]:
                return idx
            leftsum += nums[idx]
            rightsum -= nums[idx]
        return -1