class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        top = None
        maxim = 0
        for idx in range(len(prices) - 1, -1, -1):
            maxim = max(maxim, ((top - prices[idx]) if top else 0))
            top = max(prices[idx], top if top else 0)
        return maxim