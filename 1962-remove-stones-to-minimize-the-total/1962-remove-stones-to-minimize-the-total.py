class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for idx in range(len(piles)):
            piles[idx] *= -1
        heapq.heapify(piles)
        
        for _ in range(k):
            current = heapq.heappop(piles)
            positive = -current
            
            positive = positive - (positive // 2)
            
            heapq.heappush(piles, -positive)
            
        return -sum(piles)