class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direction = "right"
        final = []
        
        
        while len(matrix) > 0:
            if len(matrix) > 0 and direction == "right":
                for elem in matrix.pop(0):
                    final.append(elem)
                direction = "down"
            if len(matrix) > 0 and direction == "down":
                for row in matrix:
                    if len(row) > 0:
                        final.append(row.pop())
                direction = "left"
            if len(matrix) > 0 and direction == "left":
                for elem in matrix.pop()[::-1]:
                    final.append(elem)
                direction = "up"
            if len(matrix) > 0 and direction == "up":
                for index in range(len(matrix) - 1, - 1, -1):
                    if len(matrix[0]) > 0:
                        final.append(matrix[index].pop(0))
                direction = "right"
        return final
        