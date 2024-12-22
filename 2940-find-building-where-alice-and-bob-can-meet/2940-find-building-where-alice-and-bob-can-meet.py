class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        
        first remove the ones where the right one is higher or equal to the left side since we can already see
        the answer to be the right
        
        for the others we first sort them by their left sides
        we do this because first we have to take care of the lower ones
        since the next 
        
        so for the invalid ones we sort them by their largest index
        
        then we go over heights in a reverse way and have a monotonic stack
        then we check if the current index corresponds to the top one on our query sorted list and when it is we do a binary search on the monotonic stack
        
        queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
        we also check conditions in which the right side is greater or equal to the left
        we find [2, 2] so the answer for this is [2]
        sorted by their second values = [[0, 1], [0, 3], [2, 4], [3, 4]]
        stack = []
        curr_idx = 5
        - remove lower from stack
        - check if the last idx in the query is equal to curr_idx if so then at 
        
        stack = [5]
        curr_idx = 4
        r
        
        
        PSEUDO_CODE
        answer = [-1] * length of queries
        new_queries = []
        for left, right in queries:
        left = min(left, right)
        right = max(left, right)
        if val_left <= val_right:
        answer = right
        else:
        new_queries.append[idx, left, right]
        
        stack = []
        for idx in reverse of heights:
        while stack and stack[-1] <= height[idx]:
        pop
        
        while queries and queries[-1][-1] == idx:
        query_idx, left, right = pop
        
        ans = binary_search(val_left, stack)
        answer[q_idx] = ans
        
        stack.append(idx)
        
        return ans
        """
        answer = [-1] * len(queries)
        new_queries = []
        
        for idx, query in enumerate(queries):
            left = min(query[0], query[1])
            right = max(query[0], query[1])
            
            if heights[left] < heights[right] or left == right:
                answer[idx] = right
            else:
                new_queries.append([idx, left, right])
                
        stack = []
        new_queries.sort(key = lambda query: query[-1])
        
        def binary_search(target, idxs):
            left, right = 0, len(idxs) - 1
            best = -1
            
            while (left <= right):
                mid = (left + right) // 2
                
                val = heights[idxs[mid]]
                if val <= target:
                    right = mid - 1
                else:
                    best = idxs[mid]
                    left = mid + 1
            
            return best
        
        for idx in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] <= heights[idx]:
                stack.pop()
                
            while new_queries and new_queries[-1][-1] == idx:
                q_idx, left, right = new_queries.pop()
                ans = binary_search(heights[left], stack)
                
                answer[q_idx] = ans
                
            stack.append(idx)
            
        return answer