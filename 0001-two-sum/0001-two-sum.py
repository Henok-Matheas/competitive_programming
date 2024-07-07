class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[val, idx] for idx, val in enumerate(nums)]
        new_nums.sort()
        left, right = 0, len(nums) - 1
        
        
        while left < right:
            _sum = new_nums[left][0] + new_nums[right][0]
            
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return [new_nums[left][1], new_nums[right][1]]
            
        return None