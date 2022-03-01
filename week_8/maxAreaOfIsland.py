class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        bound = lambda row, column: row < len(
            grid) and row >= 0 and column < len(grid[0]) and column >= 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # total = []

        maxim = 0
        for i in range(len(grid)):

            def recur(rw, cl):
                grid[rw][cl] = 0
                total.append(1)

                for direction in directions:
                    row = rw + direction[0]
                    column = cl + direction[1]

                    if not bound(row, column) or grid[row][column] != 1:
                        continue
                    recur(row, column)

            for j in range(len(grid[i])):

                if grid[i][j] == 1:

                    total = []
                    recur(i, j)

                    value = 0
                    for root in total:
                        value += root
                    maxim = max(maxim, value)

        return maxim
