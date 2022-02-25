from math import ceil


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        macs = max(nums)

        left = 1
        right = max(nums)
        best_div = 0

        while left <= right:
            mid = (left + right) // 2
            tot = 0
            for i in nums:
                tot += ceil(i / mid)

            if tot > threshold:
                left = mid + 1
            else:
                best_div = mid
                right = mid - 1
        return best_div
