import heapq


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)

        popped = -1 * heapq.heappop(nums)
        for i in range(k - 1):
            popped = -1 * heapq.heappop(nums)
        return popped