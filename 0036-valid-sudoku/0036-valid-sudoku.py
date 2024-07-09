class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {idx: set() for idx in range(len(board))}
        sub_boxes = {idx: set() for idx in range(len(board))}
        
        for row_idx, row in enumerate(board):
            row_set = set()
            for col, num in enumerate(row):
                sub_idx = (row_idx // 3) * 3 + col // 3
                if num == ".":
                    continue
                    
                if num in row_set or num in cols[col] or num in sub_boxes[sub_idx]:
                    return False
                
                sub_boxes[sub_idx].add(num)
                row_set.add(num)
                cols[col].add(num)
                
        return True