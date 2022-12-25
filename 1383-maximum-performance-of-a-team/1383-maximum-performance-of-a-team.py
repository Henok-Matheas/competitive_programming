class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        maxim = 0
        sum_ = 0
        heap = []
        indices = [idx for idx in range(len(speed))]
        
        indices.sort(key = lambda idx : [efficiency[idx], speed[idx]], reverse = True)
        
        for idx in indices:
            curr_speed, curr_eff = speed[idx], efficiency[idx]
            sum_ += curr_speed
            
            maxim = max(maxim, curr_eff * sum_)
            
            heapq.heappush(heap, curr_speed)
            
            while len(heap) > k - 1:
                sum_ -= heapq.heappop(heap)
            
            
        return maxim % (7 + 10 ** 9)