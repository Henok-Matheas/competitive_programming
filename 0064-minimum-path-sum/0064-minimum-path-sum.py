class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # right, down
        directions = [[0, 1], [1,0]]
        bound = lambda row, column : row >= 0 and row < len(grid) and column >= 0 and column < len(grid[0])
        parents = collections.deque([])
        children = collections.deque([])
        parents.append([0,0])
        visited = set()
        visited.add((0,0))
        while parents or children:
            while parents:
                element = parents.popleft()
                lft = 10000000 if element[1] == 0 else grid[element[0]][element[1] - 1]
                tp = 10000000 if element[0] == 0 else grid[element[0] - 1][element[1]]
                
                grid[element[0]][element[1]] = grid[element[0]][element[1]] + (min(lft,tp) if lft != 10000000 or tp != 10000000 else 0)
                
                for direction in directions:
                    rw = element[0] + direction[0]
                    clmn = element[1] + direction[1]
                    
                    if not bound(rw,clmn) or (rw,clmn) in visited:
                        continue
                    children.append([rw,clmn])
                    visited.add((rw,clmn))
            while children:
                child = children.popleft()
                parents.append(child)
        return grid[-1][-1]