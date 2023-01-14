class Solution:
    def invalid(self, row, col, grid):
        return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        given a grid
        each cell 0 - empty, 1 -> obstacle
        4 dir
        min obstacles to remove so as to move from the upper left, to lower right.
        
        
        
        dijkstra I think
        """
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        STEP, ROW, COL = grid[0][0], 0, 0
        start = (STEP, ROW, COL)
        END = (len(grid) - 1, len(grid[0]) - 1)
        visited = set()
        heap = [start]
        
        while heap:
            step, row, col = heapq.heappop(heap)
            
            if (row, col) in visited:
                continue
                
            if (row, col) == END:
                return step
                
            visited.add((row, col))
            
            for delta_row, delta_col in directions:
                new_row, new_col, new_step = row + delta_row, col + delta_col, step
                
                if self.invalid(new_row, new_col, grid):
                    continue
                
                if (new_row, new_col) in visited:
                    continue
                
                new_step += grid[new_row][new_col]
                heapq.heappush(heap, (new_step, new_row, new_col))
                
                
        return 
            