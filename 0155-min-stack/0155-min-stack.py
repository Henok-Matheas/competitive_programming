class MinStack:
    """
    we will have a minstack list
    a normal stack list
    
    if the prev element is lower than you then you are generally useless
    if the prev element in the minstack is larger than you then you will be stored
    
    
    when popping:
        we pop
        if the current length is equal to the index stored in the minstack then we pop from the minstack as well
        
    when top we just return top
    
    
    when getMin we just return getMin if the 
    """

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.minStack or val < self.stack[self.minStack[-1]]:
            self.minStack.append(len(self.stack))
            
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
        if len(self.stack) == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minStack[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()