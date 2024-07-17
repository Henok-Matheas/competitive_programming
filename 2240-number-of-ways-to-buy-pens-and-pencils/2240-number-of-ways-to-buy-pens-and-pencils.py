class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        while total >= 0:
            ways += (total) // cost2 + 1
            total -= cost1
            
        return ways