class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [[nums1[0] + nums2[0], 0, 0]]
        answer = []
        visited = set([])
        
        def add_heap(i, j):
            if i < len(nums1) and j < len(nums2) and (i, j) not in visited:
                heapq.heappush(heap, [nums1[i] + nums2[j], i, j])
                visited.add((i, j))
                
                
        while k and heap:
            sum_, i, j = heapq.heappop(heap)
            answer.append([nums1[i], nums2[j]])
            
            add_heap(i + 1, j)
            add_heap(i, j + 1)
                
            k -= 1
            
        return answer
            
            