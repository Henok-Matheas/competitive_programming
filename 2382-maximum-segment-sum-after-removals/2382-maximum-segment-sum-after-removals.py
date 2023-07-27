class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        """
        nums
        removeQueries
        
        query[i] = remove nums[query[i]], and split into segments
        
        segment is like substring
        
        thought:
        what if you had a prefix_sum
        and every time you separate into segments you add them into a segments heap
        
        problem: time complexity when you want to find a specific segment from the heap
        solution: what if you had a sorted dict/list and everytime you separate into segments you remove the segment to be separated separate it and add it back into the sorted dict
        
        this would reduce the time complexity required to find the segment to log(n)
        
        this could work
        
        
        thought 2
        another idea. since the final output or output[-1] is always going to be zero when we remove every element what if we built up from the last removal to the first.
        
        this way when starting from the last removed, we know that every other element is removed, so we will only have a single segment, and for the other removed we know what segment they have been removed from because we know their neighbours. and what we have to do is combine those separated segments together using union find.
        
        
        query from last to first
            current query 
            prev_neigh, next_neigh = current - 1, current + 1
            if prev_neigh exists:
                unionfind
            if next_neigh exists
                unionfind
            get max_sum
        
        """
        answer = [0] * len(nums)
        max_segment = 0
        exists = set()
        parents = [idx for idx in range(len(nums))]
        segment_sum = nums[:]
        
        def find(node):
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return
            
            if segment_sum[parent2] > segment_sum[parent1]:
                parent1, parent2 = parent2, parent1
            
            parents[parent2] = parent1
            segment_sum[parent1] += segment_sum[parent2]
        
        for idx in range(len(nums) - 1, - 1, - 1):
            answer[idx] = max_segment
            
            query = removeQueries[idx]
            exists.add(query)
            
            if query + 1 in exists:
                union(query, query + 1)
            
            if query - 1 in exists:
                union(query - 1, query)
                
            max_segment = max(max_segment, segment_sum[find(query)])
            
            
        return answer
            