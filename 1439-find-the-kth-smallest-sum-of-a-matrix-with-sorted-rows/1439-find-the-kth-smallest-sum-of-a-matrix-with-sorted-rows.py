class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        m * n matrix

        
        telling anything from the matrix is hard.
        """
        
        def combine(nums1, nums2, k):
            heap = [[nums1[0] + nums2[0], 0, 0]]
            answer = []
            
            def push(i, j):
                if i < len(nums1) and j < len(nums2):
                    heapq.heappush(heap, [nums1[i] + nums2[j], i, j])
            
            while k and heap:
                sum_, i, j = heapq.heappop(heap)
                answer.append(sum_)
                
                push(i, j + 1)
                if j == 0:
                    push(i + 1, 0)
                    
                k -= 1
                    
            return answer
        
        answer = mat[0]
        for row in range(1, len(mat)):
            answer = combine(answer, mat[row], k)
            
        return answer[k - 1]
                