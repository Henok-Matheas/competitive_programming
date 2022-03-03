class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def right(row, column):
            for i in range(column):
                if grid[0][i] == 1:
                    recur(0, i)
                if grid[row - 1][i] == 1:
                    recur(row - 1, i)

        def down(row, column):
            for i in range(row):
                if grid[i][0] == 1:
                    recur(i, 0)
                if grid[i][column - 1] == 1:
                    recur(i, column - 1)

        bound = lambda row, column: row < len(
            grid) and row >= 0 and column < len(grid[0]) and column >= 0

        def recur(rw, cl):
            grid[rw][cl] = 0
            for direction in directions:
                row = rw + direction[0]
                column = cl + direction[1]
                if not bound(row, column) or grid[row][column] != 1:
                    continue
                recur(row, column)

        rw = len(grid)
        cl = len(grid[0])
        right(rw, cl)
        down(rw, cl)

        count = 0
        for row in range(rw):
            for column in range(cl):
                if grid[row][column] == 1:
                    count += 1
                # elif board[row][column] == "Y":
                #     board[row][column] = "O"
        return count
