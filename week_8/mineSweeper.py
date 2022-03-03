class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dict = {"M":"X",
               "E":"B"}
        
        row = click[0]
        column = click[1]
        
        #left, right, up, down,left_up,left_down, right_up,right_down
        directions = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]]
        
        bound = lambda row, column : row >= 0 and row < len(board) and column >= 0 and column < len(board[0])
        
        def recur(rw,cl):
            #handle for the ones that have adjecent
            count = 0
            listi = []
            for direction in directions:
                row = rw + direction[0]
                column = cl + direction[1]
                
                if not bound(row,column):
                    continue
                elif board[row][column] == "M":
                    count += 1
                elif board[row][column] == "E":
                    listi.append([row,column])
                else:
                    continue
                    
            if count == 0:
                board[rw][cl] = "B"
                for (row,column) in listi:
                    recur(row,column)
            else: board[rw][cl] = str(count)
            
        
        
        if board[row][column] == "M":
            board[row][column] = "X"
        else:
            recur(row,column)
            
        return board