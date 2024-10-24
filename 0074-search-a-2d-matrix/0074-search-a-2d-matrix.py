class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            print(mid)
            left, right = 0, len(matrix[mid]) - 1

            left_val, right_val = matrix[mid][left], matrix[mid][right]

            if target < left_val:
                bottom = mid - 1
                continue
            elif target > right_val:
                top = mid + 1
                continue

            while left <= right:
                col_mid = (left + right) // 2

                val = matrix[mid][col_mid]

                if val == target:
                    return True
                elif val < target:
                    left = col_mid + 1
                else:
                    right = col_mid - 1
            return False

        return False