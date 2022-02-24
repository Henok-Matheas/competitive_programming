import heapq


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx in range(len(stones)):
            stones[idx] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            if first - second > 0:
                heapq.heappush(stones, second - first)

        # for idx in range(len(stones)):
        #     stones[idx] = -1 * stones[idx] if stones[idx] < 0 else stones[idx]
        return -1 * stones[0] if len(stones) > 0 else 0
