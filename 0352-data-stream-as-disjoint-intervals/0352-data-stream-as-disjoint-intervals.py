class SummaryRanges:
    """
    ai >= 0
    
    summarize nums seen so far as alist of disjoint intervals
    
    addNum add num to stream
    
    getIntervals gives list of intervals
    """

    def __init__(self):
        LENGTH = 10 ** 4 + 1
        self.values = [False] * LENGTH
    def addNum(self, value: int) -> None:
        self.values[value] = True

    def getIntervals(self) -> List[List[int]]:
        stack = []
        
        for num, exists in enumerate(self.values):
            if not exists:
                continue
            
            if not stack or stack[-1][-1] != num - 1:
                stack.append([num, num])
                
            stack[-1][-1] = num
                
        
        return stack


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()