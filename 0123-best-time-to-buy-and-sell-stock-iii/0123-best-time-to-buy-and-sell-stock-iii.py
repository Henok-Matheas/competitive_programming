class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
