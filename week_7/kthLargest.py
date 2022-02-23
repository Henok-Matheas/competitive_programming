import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        for index in range(len(nums)):
            nums[index] = -1 * nums[index]
        heapq.heapify(nums)
        self.nums = nums
        self.discarded = []
        for i in range(self.k - 1):
            heapq.heappush(self.discarded, -1 * heapq.heappop(self.nums))

    def add(self, val: int) -> int:
        while len(self.discarded) < self.k - 1:
            heapq.heappush(self.discarded, -1 * heapq.heappop(self.nums))

        if self.discarded and val >= self.discarded[0]:
            heapq.heappush(self.discarded, val)

        else:
            heapq.heappush(self.nums, -1 * val)

        while len(self.discarded) > self.k - 1:
            heapq.heappush(self.nums, -1 * heapq.heappop(self.discarded))

        return -1 * self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)