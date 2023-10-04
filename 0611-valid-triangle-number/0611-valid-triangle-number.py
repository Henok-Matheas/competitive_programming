class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        
        for c in range(2, len(nums)):
            a = 0
            for b in range(c - 1, 0, -1):
                a = min(b - 1, a)
                while a < b and nums[a] + nums[b] <= nums[c]:
                    a += 1
                    
                total += (b - a)
                
        return total