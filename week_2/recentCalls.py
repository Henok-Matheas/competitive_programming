class RecentCounter:

    def __init__(self):
        self.queue = []
        self.index = 0
        

    def ping(self, t: int) -> int:
        
        (self.queue).append(t)
        for i in range(self.index, len(self.queue)):
            if self.queue[i] >= self.queue[-1] - 3000:
                self.index = i
                return len(self.queue) - self.index
        
        
        
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)