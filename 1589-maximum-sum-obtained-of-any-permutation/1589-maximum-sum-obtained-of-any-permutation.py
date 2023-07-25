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
        N = len(nums)
        total = 0
        nums.sort()
        counts = [0] * (N + 1)
        
        for start, end in requests:
            counts[end + 1] -= 1
            counts[start] += 1
            
        for idx in range(1, N + 1):
            counts[idx] += counts[idx - 1]
        
        counts.pop()
        counts.sort()
        
        for count, value in zip(counts,nums):
            total += count * value
            
        return total % (10 ** 9 + 7)
        
        
        
            
        