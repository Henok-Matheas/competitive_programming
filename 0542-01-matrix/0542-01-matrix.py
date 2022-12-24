class Solution:
    def invalid(self, row, col, graph):
        return not(0 <= row < len(graph) and 0 <= col < len(graph[0]))
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distances = [[0] * len(mat[0]) for _ in range(len(mat))]
        queue = deque([])
        distance = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for rw, row in enumerate(mat):
            for cl, cell in enumerate(row):
                if not cell:
                    queue.append([rw, cl, distance])
                    
        while queue:
            row, col, distance = queue.popleft()
            distances[row][col] = distance
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                new_distance = distance + 1
                
                if self.invalid(new_row, new_col, mat):
                    continue
                    
                if mat[new_row][new_col]:
                    mat[new_row][new_col] = 0
                    queue.append([new_row, new_col, new_distance])
                    
        
        return distances