class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in range(len(grid)):

            left = 0
            right = len(grid[row]) - 1
            least = None

            if grid[row][0] < 0:
                max_row = len(grid) - 1
                m = max_row - row + 1
                n = len(grid[row])
                count += (m * n)
                return count

            while left <= right:
                column = (left + right) // 2

                if grid[row][column] >= 0:
                    left = column + 1
                else:
                    least = column
                    right = column - 1
            count += len(grid[row]) - least if not least == None else 0

        return count