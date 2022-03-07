import heapq


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        visited = set()

        working = []
        heapq.heappush(working, [grid[0][0], [0, 0]])

        bound = lambda row, column: row >= 0 and row < len(
            grid) and column >= 0 and column < len(grid)

        while working:
            now = heapq.heappop(working)

            if str(now[1][0]) + " " + str(now[1][1]) in visited:
                continue
            visited.add(str(now[1][0]) + " " + str(now[1][1]))

            level = max(now[0], grid[now[1][0]][now[1][1]])
            if now[1] == [len(grid) - 1, len(grid) - 1]:
                return level
            for direction in directions:
                row = now[1][0] + direction[0]
                column = now[1][1] + direction[1]

                if not bound(
                        row,
                        column) or str(row) + " " + str(column) in visited:
                    continue

                heapq.heappush(working, [level, [row, column]])
        return answer