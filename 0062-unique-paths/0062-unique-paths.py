class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## bottom up approach
        
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] += (dp[j - 1] if j - 1 >= 0 else 0)
        return dp[n - 1]