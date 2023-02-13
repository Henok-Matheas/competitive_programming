class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = collections.deque()
        visited = set()
        
        if grid[0][0] != 0:
            return -1
        
        directions = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
        valid = lambda row, column : 0 <= row < len(grid) and 0 <= column < len(grid[0])
        
        queue.append((0,0,1))
        visited.add((0,0))
        
        
        goal = (len(grid) - 1, len(grid[0]) - 1)
        while queue:
            cell = queue.popleft()
            row = cell[0]
            column = cell[1]
            length = cell[2]
            
            if (row,column) == goal:
                return length if grid[row][column] == 0 else -1
            
            
            for direction in directions:
                newRow = row + direction[0]
                newCol = column + direction[1]
                
                if (newRow, newCol) in visited or not valid(newRow,newCol) or grid[newRow][newCol] != 0:
                    continue
                    
                visited.add((newRow,newCol))
                queue.append((newRow,newCol, length + 1))
                
                
                
        return -1
            