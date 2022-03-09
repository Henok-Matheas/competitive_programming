class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        heap = []
        for point in points:
            heapq.heappush(heap, [point[1], point[0]])
        arrow = 0
        begin = None
        end = None
        while heap:
            curr = heapq.heappop(heap)
            if arrow == 0 or end < curr[1]:
                begin = curr[1]
                end = curr[0]
                arrow += 1
        return arrow
