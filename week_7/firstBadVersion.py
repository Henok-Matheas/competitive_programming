# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:

    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        first = 1

        while left <= right:
            mid = (left + right) // 2

            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
                first = mid
        return first
