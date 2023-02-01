class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        it's a window for the col and the row
        
        for every col we do row wise sum
        
        two while loops one for the col, and the other for the row
        they try to find the right bound, we also have pointers to the left, and up
        when the bound is reached we include them
        """
        """
        we first create the col wise sum
        
        we then create the row wise sum using the same function
        """
        m, n = len(mat), len(mat[0])
        
#         -1, 0, 1
#         -1, 0, 1
        
        
#         3   6   5
#         9   15  11
#         15  24  17
        
        rows = []
        answer = mat[::]
        for rw, row in enumerate(mat):
            left, right = 0, 0
            sum_ = 0
            cols = []
            for col, cell in enumerate(row):
                while right <= min(n - 1, col + k):
                    sum_ += row[right]
                    right += 1
                
                cols.append(sum_)
                if left == col - k:
                    sum_ -= row[left]
                    left += 1
                    
            rows.append(cols)
            
        for col in range(len(mat[0])):
            top, bottom = 0, 0
            sum_ = 0
            for row in range(len(mat)):
                while bottom <= min(m - 1, row + k):
                    sum_ += rows[bottom][col]
                    bottom += 1
                
                answer[row][col] = sum_
                if top == row - k:
                    sum_ -= rows[top][col]
                    top += 1
                    
                    
        return answer
        
            
        
                    