class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        (0, 0) faced north
        north = (-1, 0)
        south = (1, 0)
        east = (0, 1)
        west = (0, -1)
        
        robot recieve:
        G -> 1 unit
        L -> turn left 90 deg
        R -> turn right 90 deg
        
        performs instructions in order
        
        (-1, 0)
        (-2, 0)
        (0, 0)
        
        one approach:
        will it ever be bound if it doesn't end at the same place??
        
        (-1, 0)
        <-
        
        first approach doesn't work. why?
            - because we can have
            
            
        do it four times if it returns valid if not invalid
        
        """
        start = (0, 0)
        row, col = 0, 0
        dir_row, dir_col = -1, 0
        TRIP = 4
        
        for _ in range(TRIP):
            for instruction in instructions:
                if instruction == "G":
                    row += dir_row
                    col += dir_col
                    continue
                elif instruction == "L":
                    dir_col *= -1
                else:
                    dir_row *= -1
                
                dir_row, dir_col = dir_col, dir_row
        
        return (row, col) == start