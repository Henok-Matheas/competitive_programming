class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        you just need a right product array
        
        
        for every number we will have a left product using prefix sum kind of thing and then with the right product we can 
        
        if we do it in the same array it will be
        """
        product = [1] * len(nums)
        right, left = 1, 1
        
        for idx in range(len(nums) - 1, -1, -1):
            product[idx] = right
            right *= nums[idx]
            
            
        for idx, num in enumerate(nums):
            product[idx] *= left
            left *= num
            
        return product
        