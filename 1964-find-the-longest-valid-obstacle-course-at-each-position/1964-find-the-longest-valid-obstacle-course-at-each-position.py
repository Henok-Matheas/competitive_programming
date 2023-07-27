class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        obstacles list with height
        
        for every index find length of longest obstacle course
            - choose obstacles [0 - i]
            - include obstacle at index
            - follow the same order
            - obstacle[i] <= obstacle[i - 1]
            
        simpler question
            for every index
                longest increasing subsequence
                
        
        longest increasing subsequence:
            we will have a monotonic stack and in that monotonic stack we look for the lowest element that is higher than us.
            if it exists:
                replace it with us, and use that index as the length
            else:
                append us, and use the length as the index
                
                
        can't we do it in a dp way?
        """
        answer = [0] * len(obstacles)
        monotonic_stack = []
        
        
        def binary(target, array):
            left, right = 0, len(array) - 1
            best = len(array)
            
            while left <= right:
                mid = (left + right) // 2
                
                if array[mid] <= target:
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1
                    
            return best
        
        
        for idx, val in enumerate(obstacles):
            placing_idx = binary(val, monotonic_stack)
            if placing_idx == len(monotonic_stack):
                monotonic_stack.append(0)
            
            monotonic_stack[placing_idx] = val
            answer[idx] = placing_idx + 1
            
        return answer