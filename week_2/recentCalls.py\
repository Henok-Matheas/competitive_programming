class RecentCounter:

    def __init__(self):
        self.pings = []
        

    def ping(self, t: int) -> int:
        cnt = 0
        (self.pings).append(t)
        for j in range(len(self.pings), 0, -1):
            if self.pings[j - 1] > t - 3001:
                cnt += 1
                # print(t, self.pings[j - 1],cnt)
            else:
                break
        return cnt
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)