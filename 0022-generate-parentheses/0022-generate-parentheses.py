class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, stack = [], []
        
        def backtrack(left = 0, right = 0):
            if len(stack) == 2 * n:
                ans.append("".join(stack))
                return 
            if left > right:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
        backtrack()
        return ans
        
        