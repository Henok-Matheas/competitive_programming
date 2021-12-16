class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        (self.stack).append(x)
        self.queue = self.stack[::-1]
        

    def pop(self) -> int:
        popped = (self.queue).pop()
        self.stack = self.queue[::-1]
        return popped
        

    def peek(self) -> int:
        return self.queue[-1]
        