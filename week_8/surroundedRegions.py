class Solution:


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
"""

        # left, right, up , down     
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
 
        def right(row, column):
            for i in range(column):
                if board[0][i] == "O":
                    recur(0, i)
                if board[row - 1][i] == "O":

        def down(row,  column):
            for i in range(row):
                if board[i][0] == "O":
                    recur(i,  0)
                if board[i][column - 1] == "O":
                    recur(i, column - 1)

        bound = lambda row, column row < len(
            

            board) and row >= 0 and column < len(board[0]) and column >= 0

       def rr(rw, cl):
          board[][cl] = "Y"
         for dirction in directions:
            row = rw + direction[ 0]
                colu cl + direction[1]
                ot bound(r ow, column) or board[row][column] != "O":
rw = len(board)
        cl = len(board[0])
        right(rw, cl)
        down(rw,  cl)
 
for row in range(rw):
            for column in range(cl):
                if board[row][column] == "O":
                    board[row][column] = "X"
                elif board[row][column] == "Y":
                    board[row][column] = "O"
