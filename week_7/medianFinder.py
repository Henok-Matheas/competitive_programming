from math import ceil
import heapq


class MedianFinder:

    def __init__(self):
        self.nums = []
        self.discarded = []
        self.index = 0

    def addNum(self, num: int) -> None:
        if len(self.nums) <= ceil(self.index / 2):
            heapq.heappush(self.nums, num)

        elif len(self.discarded) <= ceil(self.index / 2):
            heapq.heappush(self.discarded, -1 * num)

        while self.nums and len(self.nums) > ceil(self.index / 2):
            heapq.heappush(self.discarded, -1 * heapq.heappop(self.nums))

        while self.discarded and len(self.discarded) > ceil(self.index / 2):
            heapq.heappush(self.nums, -1 * heapq.heappop(self.discarded))

        self.index += 1

    def findMedian(self) -> float:

        val1 = self.nums[0] if self.nums else None
        val2 = -1 * self.discarded[0] if self.discarded else None
        if self.index % 2 == 1:
            return val1
        else:
            return (val1 + val2) / 2 if self.nums and self.discarded else None


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()