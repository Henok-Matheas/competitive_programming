class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        score = 0
        
        one op
            - inc score by nums[i] then nums[i] = ceil(nums[i] / 3)
            
        you apply exactly k operations return max score
        """
        score = 0
        FACTOR = 3
        heap = []
        
        for num in nums:
            heapq.heappush(heap, -num)
            
        for _ in range(k):
            popped = heapq.heappop(heap)
            score += -popped
            
            heapq.heappush(heap, -math.ceil(-popped / FACTOR))
        
        
        
        return score