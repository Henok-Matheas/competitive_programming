class Solution:
    def binary(self, lst, target):
        best = -1
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if lst[mid] < target:
                best = mid
                left = mid + 1
            else:
                right = mid - 1      
        return best + 1
                
    def reversePairs(self, nums: List[int]) -> int:
        ordered = []
        pairs = 0
        for idx in reversed(range(len(nums))):
            curr = nums[idx]
            ## binary search on ordered
            pairs += self.binary(ordered, curr)
            bisect.insort(ordered, curr * 2)
            
        return pairs
            
            
        