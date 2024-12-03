class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total = 0
        goal = 1
        
        while maxDoubles and target > goal:
            if target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
                
            total += 1
        
        return total + (target - goal)