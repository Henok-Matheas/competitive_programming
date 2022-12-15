class Solution:
    def calculate(self, s: str) -> int:
        
        def findNumber(idx):
            j = idx
            while j < len(s) and s[j].isnumeric():
                j += 1
            return j - 1, int(s[idx: j])
        
        
        def evaluate(idx):
            if idx >= len(s):
                return 0
            
            stack = [0]
            operations = ["+"]
            
            j = idx
            
            while j < len(s):
                curr = None
                
                if s[j] == "+" or s[j] == "-":
                    operations.append(s[j])
                    
                if s[j] == ")":
                    return j, stack.pop()
                
                if s[j].isnumeric():
                    j, curr = findNumber(j)
                    
                if s[j] == "(":
                    j, curr = evaluate(j + 1)
                    
                    
                if curr is not None:
                    prev, op = stack.pop(), operations.pop()
                    final = eval(str(prev) + op + str(curr))
                    stack.append(final)
                    
                j += 1
                    
                
            return j, stack.pop()
        
        return evaluate(0)[-1]