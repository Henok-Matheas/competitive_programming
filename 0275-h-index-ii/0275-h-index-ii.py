class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        best = 0
        while left <= right:
            mid = (left + right) // 2
            val = citations[mid]
            cit = len(citations) - mid
            
            if val >= cit:
                best = cit
                right = mid - 1
            else:
                left = mid + 1
            
        return best
            