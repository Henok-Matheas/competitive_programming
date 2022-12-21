class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        maxim = -float("inf")
        max_range = [-float("inf"), float("inf")]
        
        
        for idx, row in enumerate(nums):
            col = 0
            val = row[col]
            heapq.heappush(heap, [val, idx, col])
            maxim = max(maxim, val)
            
            
        while heap:
            val, row, col = heapq.heappop(heap)
            if maxim - val < max_range[1] - max_range[0]:
                max_range = [val, maxim]
                
            if col + 1 == len(nums[row]):
                return max_range
            
            col += 1
            val = nums[row][col]
            
            heapq.heappush(heap, [val, row, col])
            maxim = max(maxim, val)
            
        return max_range
            