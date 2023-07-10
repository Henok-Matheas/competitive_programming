class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [0]
        minim = len(nums) + 1
        
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
            
            
        def binary(start, curr, prefix):
            left, right = start, len(prefix) - 1
            best = len(prefix) + start
            
            while left <= right:
                mid = (left + right) // 2
                
                mid_sum = prefix[mid] - curr

                if mid_sum < target:
                    left = mid + 1

                else:
                    best = mid
                    right = mid - 1

            return best
            
            
        for idx, curr in enumerate(prefix_sum):
            end = binary(idx, curr, prefix_sum)
            
            minim = min(minim, end - idx)
                
        return 0 if minim == len(nums) + 1 else minim