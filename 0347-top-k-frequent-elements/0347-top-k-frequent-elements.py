class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        
        for num in counts:
            heapq.heappush(heap, [counts[num], num])
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        
        
        return [val for count, val in heap]