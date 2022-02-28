class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        left = min(nums)
        right = max(nums)

        best = 0

        while left <= right:
            mid = (left + right) // 2

            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return best