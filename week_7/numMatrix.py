class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = []

        for row in range(len(matrix)):
            temp = []
            for column in range(len(matrix[-1])):
                prev = temp[-1] if temp else 0
                temp.append(prev + matrix[row][column])
            self.matrix.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            sum += self.matrix[row][col2] - (self.matrix[row][col1 - 1]
                                             if col1 > 0 else 0)
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)