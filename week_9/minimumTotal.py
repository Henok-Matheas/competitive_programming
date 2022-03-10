class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        visited = defaultdict(bool)

        def recur(row, column):
            if row == len(triangle) - 1:
                return triangle[row][column]

            curr = triangle[row][column]

            if (row + 1, column) not in visited:
                visited[(row + 1, column)] = recur(row + 1, column)
            if (row + 1, column + 1) not in visited:
                visited[(row + 1, column + 1)] = recur(row + 1, column + 1)

            return min(visited[row + 1, column], visited[row + 1,
                                                         column + 1]) + curr

        return recur(0, 0)
