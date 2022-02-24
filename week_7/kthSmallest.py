import heapq


class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lists = []
        for i in matrix:
            for j in i:
                heapq.heappush(lists, j)

        # print(lists)
        for j in range(k - 1):
            heapq.heappop(lists)
        return lists[0] if lists else None
