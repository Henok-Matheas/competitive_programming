class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '/': lambda x, y:  math.trunc(x / y),
              '*': lambda x, y: x * y}
        stack = []
        
        for i in tokens:
            try:
                inti = int(i)
                stack.append(inti)
            except:
                y = stack.pop()
                x = stack.pop()
                output = ops[i](x, y)
                stack.append(output)
                
        return stack[0]