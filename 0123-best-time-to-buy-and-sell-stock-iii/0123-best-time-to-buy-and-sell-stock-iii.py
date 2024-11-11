class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        have two loops beka
        
        first loop we will only store the lowest so far
        and do the ii 
        
        then we only store the max and do from the right side
        
        left soln
        
        
        
        
        """
        lowest, highest = max(prices), 0
        profit = [0] * len(prices)
        maxim = 0
        ## left side
        for idx, price in enumerate(prices):
            profit[idx] = max(profit[idx], price - lowest, profit[idx - 1] if idx - 1 else 0)
            lowest = min(lowest, price)
            maxim = max(maxim, profit[idx])
            
        ## right side 
        
        for idx in range(len(prices) - 1, 0, -1):
            curr_profit = profit[idx - 1]
            curr_profit += max(0, highest - prices[idx])
            highest = max(highest, prices[idx])
            
            maxim = max(maxim, curr_profit)
        
        return maxim
        
        allowed = 2

        @lru_cache(None)
        def dp(index, buy, k):
            if not k:
                return 0
            if index >= len(prices):
                return 0

            sell = not buy
            if buy:
                return max(-prices[index] + dp(index + 1, sell, k), dp(index + 1, buy, k))
            else:
                return max(prices[index] + dp(index + 1, sell, k - 1), dp(index + 1, buy, k))

        return dp(0, True, allowed)
