class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:

        limi = -1 * limit

        heapy = []
        minheap = []
        for i in people:
            heapq.heappush(heapy, -1 * i)

        count = 0
        while heapy:
            curr = heapq.heappop(heapy)

            if minheap and -1 * minheap[0] + curr >= limi:
                count += 1
                heapq.heappop(minheap)
            else:
                heapq.heappush(minheap, -1 * curr)
        while minheap:
            minheap.pop()
            count += 1
        return count