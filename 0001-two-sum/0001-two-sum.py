class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for idx, num in enumerate(nums):
            if target - num in hashmap:
                return [idx, hashmap[target - num]]
            
            hashmap[num] = idx
            
        return None