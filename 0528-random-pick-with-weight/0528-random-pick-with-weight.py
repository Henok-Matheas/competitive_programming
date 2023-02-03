class Solution:
    """
    weights
    
    pickIndex randomly picks index and returns it
    probability[i] = w[i] / sum(w)
    what if we create a list of size sum(w)
    
    we just need to know the sum and the weight
    
    so after we know that based on the ratio of sum to weight 
    we will have a new array
    
    so for every index
     we will append a new array of size int(weight * len(array) * 100/ sum )
    """

    def __init__(self, w: List[int]):
        ## list fo indices
        self.array = []
        self.SUM = sum(w)
        self.LENGTH = len(w)
        self.PERCENT = 100
        
        for idx, weight in enumerate(w):
            self.array += [idx] * math.ceil(weight * self.LENGTH * self.PERCENT / self.SUM)
        

    def pickIndex(self) -> int:
        return self.array[random.randrange(len(self.array))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()