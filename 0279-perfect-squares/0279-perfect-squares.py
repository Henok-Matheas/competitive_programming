class Solution:
    def numSquares(self, n: int) -> int:
        """
        this question is basically coin change, but we precompute the initial coins that we have.
        
        
        for every sum we will check the least amount of coins we can have when using different coins
        
        """
        
        squares = [idx ** 2 for idx in range(1, int(sqrt(n)) + 1)]
        sums = [idx for idx in range(n + 1)]
        sums[0] = 1
        
        for sum_ in range(n + 1):
            for square in squares:
                if sum_ == square:
                    sums[sum_] = 1
                    
                elif sum_ - square >= 0:
                    sums[sum_] = min(sums[sum_], sums[sum_ - square] + sums[square])
                    
                    
        return sums[n]