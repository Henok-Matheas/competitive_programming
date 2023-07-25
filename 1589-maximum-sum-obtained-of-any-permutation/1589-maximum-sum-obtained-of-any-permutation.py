class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        have a (count, idx) list
        
        sort the requests and do the count thing
        
        sort it
        sort nums
        
        do the prefix sum for the new nums
        
        then it's just answering the requests
        """
        
        starts = {}
        ends = {}
        
        for start, end in requests:
            if start not in starts:
                starts[start] = 0
                
            if end not in ends:
                ends[end] = 0
                
            starts[start] += 1
            ends[end] += 1
            
        starting = min(starts)
        ending = max(ends)
        counts = [0] * len(nums)
        count = 0
        
        
        for idx in range(len(nums)):
            count += starts.get(idx, 0)
            counts[idx] = count
            count -= ends.get(idx, 0)
            
        indices = [idx for idx in range(len(nums))]
        indices.sort(key = lambda idx: counts[idx])
        nums.sort()
        new_nums = [0] * len(nums)
        
        for idx, indice in enumerate(indices):
            new_nums[indice] = nums[idx]
            
        prefix_sum = [0] * (len(nums) + 1)
        
        for idx, val in enumerate(new_nums):
            prefix_sum[idx + 1] = prefix_sum[idx] + val
            
        total = 0
        
        for start, end in requests:
            total += prefix_sum[end + 1] - prefix_sum[start]
            
        return total % (10 ** 9 + 7)
        
        
        
            
        