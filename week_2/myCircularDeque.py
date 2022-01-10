class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.i = None
        self.j = None
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.i, self.j = 0, 0
            self.deque[self.j] = value
            return True
        self.j = (self.j + 1) % self.k
        self.deque[self.j] = value
        return True
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.i, self.j = 0, 0
            self.deque[self.i] = value
            return True
        self.i = (self.i - 1 + self.k) % self.k
        self.deque[self.i] = value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            self.i, self.j = None, None
            return False
        self.deque[self.j] = None
        self.j = (self.j - 1 + self.k) % self.k
        if self.isEmpty():
            self.i, self.j = None, None
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            self.i, self.j = None, None
            return False
        self.deque[self.i] = None
        self.i = (self.i + 1) % self.k
        if self.isEmpty():
            self.i, self.j = None, None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.j]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.i]
        

    def isEmpty(self) -> bool:
        if self.i == self.j and self.i == None:
            return True
        elif self.i == self.j and (self.deque[self.i] == None or self.deque[self.j] == None):
            return True
        elif (self.deque).count(None) == self.k:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.i == None:
            return False
        return (self.j + 1 + self.k) % self.k == self.i or (self.i - 1 + self.k) % self.k == self.j
         


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
