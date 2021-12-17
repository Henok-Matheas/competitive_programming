class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or val < self.stack[-1][1]:
            pushed = (self.stack).append([val,val])
        else:
            pushed = (self.stack).append([val,self.stack[-1][1]])

    def pop(self) -> None:
        popped = (self.stack).pop()
        

    def top(self) -> int:
        top_stack = (self.stack)[-1]
        return top_stack[0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]