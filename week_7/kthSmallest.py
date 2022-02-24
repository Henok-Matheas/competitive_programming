import heapq
import heapq


class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        for j in range(k - 1):
            middle = heapq.heappop(matrix)
            heapq.heappop(middle)

            if middle:
                heapq.heappush(matrix, middle)

        return matrix[0][0] if matrix and matrix[0] else None


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
