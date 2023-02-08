class Solution:
    @cache
    def dp(self, num):
        if num == 1:
            return 0

        if num % 2:
            return 1 + self.dp(num * 3 + 1)
        return 1 + self.dp(num // 2)
    
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        bruteforce is a dp approach by saving
        
        for idx in range(12, 15):
        dp(idx)
        
        dp(idx)
        if idx == 1:
        return 0
        
        if even, and if odd
        return
        
        
        sort the nums based on their values
        return nums[k - 1]
        """
        nums = []
        for num in range(lo, hi + 1):
            nums.append([self.dp(num), num])
            
        nums.sort()
        return nums[k - 1][1]
