class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tot = float("inf")
        for rowindx in range(len(triangle)):
            minim = float("inf")
            for indx in range(len(triangle[rowindx])):
                tplft = 10000000 if indx == 0 or rowindx == 0 else triangle[
                    rowindx - 1][indx - 1]
                tp = 10000000 if indx == len(
                    triangle[rowindx]) - 1 or rowindx == 0 else triangle[
                        rowindx - 1][indx]

                triangle[rowindx][indx] = triangle[rowindx][indx] + (min(
                    tplft, tp) if tplft != 10000000 or tp != 10000000 else 0)
                minim = min(minim, triangle[rowindx][indx])
            tot = minim
        return tot


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
