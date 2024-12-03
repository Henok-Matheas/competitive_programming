class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opp = {"(": ")", "[": "]", "{": "}"}
        
        for char in s:
            if char in opp:
                stack.append(opp[char])
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                return False
                
        return len(stack) == 0