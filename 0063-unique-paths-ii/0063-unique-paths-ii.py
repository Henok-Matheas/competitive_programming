class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = "I"
                
                
        obstacleGrid[0][0] = 1
                    
        def valid(row,column):
            return 0<= row < len(obstacleGrid) and 0<= column < len(obstacleGrid[0])
            
        # print(f" the grid is {obstacleGrid}")
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == "I":
                    continue
                # print(f"on index {row,col} has value {obstacleGrid[row][col]}")
                obstacleGrid[row][col] += obstacleGrid[row - 1][col] if valid(row - 1,col) and obstacleGrid[row - 1][col] != "I" else 0
                obstacleGrid[row][col] += obstacleGrid[row][col - 1] if valid(row,col - 1) and obstacleGrid[row][col - 1] != "I" else 0
                # print(f"the final of index {row,col} is {obstacleGrid[row][col]}")
                
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != "I" else 0