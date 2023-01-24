class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while stack and k and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
            
        while k and stack:
            stack.pop()
            k -= 1
            
        if not stack:
            return "0"
        
        return str(int("".join(stack)))