class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        visited = set()
        last = 0
        
        for _ in range(n):
            last = heapq.heappop(heap)
            
            for factor in [2, 3, 5]:
                if last * factor not in visited:
                    heapq.heappush(heap, last * factor)
                    visited.add(last * factor)
            
            
        return last