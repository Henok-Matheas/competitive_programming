class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_prod = [1] * (len(nums) + 1)
        answer = []
        prod = 1
        for idx in range(len(nums) - 1, -1, -1):
            r_prod[idx] = prod
            prod *= nums[idx]
        
        prod = 1
        for idx, num in enumerate(nums):
            answer.append(prod * r_prod[idx])
            prod *= num
            
        return answer
        