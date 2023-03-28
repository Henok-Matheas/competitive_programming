class Solution:
    def merger(self, nums1, nums2):
        nums = []
        right = 0
        
        for num in nums1:
            while right < len(nums2) and nums2[right] <= num:
                nums.append(nums2[right])
                right += 1
            
            nums.append(num)
        
        return nums + nums2[right:]
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        left = self.sortArray(nums[:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2:])
        
        return self.merger(left, right)
        
    