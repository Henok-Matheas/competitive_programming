class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k = len(mat1), len(mat2[0]), len(mat1[0])
        answer = [[0] * n for _ in range(m)]
        
        
        def mult(row, col, k):
            answer = 0
            
            for cell in range(k):
                answer += mat1[row][cell] * mat2[cell][col]
                
            return answer
            
            
        
        for row in range(m):
            for col in range(n):
                answer[row][col] = mult(row, col, k)
            
        
        return answer