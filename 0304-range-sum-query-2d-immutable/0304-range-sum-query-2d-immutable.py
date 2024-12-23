class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        for every row we will do the 2d prefix sum using total to have rowwise sum and then to look up to get prev prefix_sum
        """
        self.p = [[0] * (len(matrix[0]) + 1)]
        for r_idx, row in enumerate(matrix):
            total = 0
            p_row = [0]
            for c_idx, val in enumerate(row):
                total += val
                p_row.append(total + self.p[r_idx][c_idx + 1])
            self.p.append(p_row)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        for this one we have three regions
        
        r1, c1
        
        r2, c2
        
        r2 + 1, c2 + 1) - (r1, c2 + 1) - (r2 + 1, c1) + (r1, c1)
        
        (r2, c2) - (r1, c2) - (r2, c1) + (r1, c1)
        """
        row2 += 1
        col2 += 1
        return self.p[row2][col2] - self.p[row2][col1] - self.p[row1][col2] + self.p[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)