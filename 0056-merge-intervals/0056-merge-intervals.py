class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        stack = []
        
        for start, end in intervals:
            if stack and stack[-1][0] <= start <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], end)
                
            else:
                stack.append([start, end])
                
                
        return stack