class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        
        
#         ## bottom up
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for rec in range(amount + 1):
                    if rec - coin >= 0:
                        dp[rec] += dp[rec - coin]
                        # print(rec, dp[rec], dp[rec - coin],coin)
        return dp[amount]

        # ## top down
        # @lru_cache(maxsize = None)
        # def recur(sum_, index):
        #     if index >= len(coins) or sum_ >= amount:
        #         return 1 if sum_ == amount else 0
        #     return recur(sum_ + coins[index], index) + recur(sum_, index + 1)
        # return recur(0,0)
    