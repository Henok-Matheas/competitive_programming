class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column = len(matrix[0])
        left = 0
        right = len(matrix) * column - 1

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        while left <= right:
            mid = (left + right) // 2

            row = mid // column
            clm = mid % column

            if matrix[row][clm] < target:
                left = mid + 1
            elif matrix[row][clm] > target:
                right = mid - 1
            else:
                return True
        return False
