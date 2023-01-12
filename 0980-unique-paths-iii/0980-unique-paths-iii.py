class Solution:
    def inbound(self, row, col, row_bound, col_bound):
        return 0 <= row < row_bound and 0 <= col < col_bound
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        n, m = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        starting_row = starting_col = target_visited = visited = 0

        for rw, row in enumerate(grid):
            for cl, val in enumerate(row):
                if val == -1:
                    continue

                target = (rw * m) + cl + 1
                if val == 1:
                    visited |= 1 << target
                    starting_row, starting_col = rw, cl

                target_visited |= 1 << target
        
        
        def dfs(row, col, target_visited, visited):
            
            if target_visited == visited:
                return 1

            if grid[row][col] == 2:
                return 0
            
            total = 0
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                target = (new_row * m) + new_col + 1

                if not self.inbound(new_row, new_col, len(grid) , len(grid[0])):
                    continue

                if 1 << target & visited:
                    continue

                if grid[new_row][new_col] == 0 or grid[new_row][new_col] == 2:
                    total += dfs(new_row, new_col, target_visited, visited | 1 << target)
            
            return total
        
        return dfs(starting_row, starting_col, target_visited, visited)                