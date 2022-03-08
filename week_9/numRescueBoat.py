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

        people.sort()

        ppl = collections.deque(people)

        count = 0
        while ppl:
            if len(ppl) == 1:
                return count + 1

            first = ppl[0]
            last = ppl.pop()

            if first + last <= limit:
                ppl.popleft()
            count += 1
        return count