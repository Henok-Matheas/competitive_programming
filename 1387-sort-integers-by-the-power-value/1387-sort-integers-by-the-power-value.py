class Solution:
    @cache
    def dp(self, num):
        if num == 1:
            return 0

        if num % 2:
            return 1 + self.dp(num * 3 + 1)
        return 1 + self.dp(num // 2)
    
    
    def quickselect(self, left, right, nums, k):
        pivot, pointer = nums[right], left
        
        for idx in range(left, right):
            if nums[idx] <= pivot:
                nums[pointer], nums[idx] = nums[idx], nums[pointer]
                pointer += 1
                
                
        nums[pointer], nums[right] = nums[right], nums[pointer]
        
        if pointer > k:
            return self.quickselect(left, pointer - 1, nums, k)
        if pointer < k:
            return self.quickselect(pointer + 1, right, nums, k)
        
        return nums[pointer][1]
    
    
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
            
        
        return self.quickselect(0, len(nums) - 1, nums, k - 1)
