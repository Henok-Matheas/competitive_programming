class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        heap = [(0,0,0)]
        visited = set([])
        
        while heap:
            max_, row, col = heapq.heappop(heap)
            
            if (row, col) in visited:
                continue
                
            visited.add((row, col))
            
            if (row, col) == (len(heights) - 1, len(heights[0]) - 1):
                return max_
            
            for deltar, deltac in directions:
                new_row, new_col = row + deltar, col + deltac
                
                if (new_row, new_col) in visited:
                    continue
                    
                if 0 <= new_row < len(heights) and 0 <= new_col < len(heights[0]):
                    max_new = max(max_, abs(heights[row][col] - heights[new_row][new_col]))
                    heapq.heappush(heap, [max_new, new_row, new_col])