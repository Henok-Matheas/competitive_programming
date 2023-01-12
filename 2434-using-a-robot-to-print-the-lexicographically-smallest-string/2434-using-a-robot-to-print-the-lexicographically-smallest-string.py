class Solution:
    def robotWithString(self, s: str) -> str:


        ## stores char and idx
        heap = []

        for idx, char in enumerate(s):
            heapq.heappush(heap, [char, idx])
            
        prev_idx = -1
        ## stores idx
        visited = set()
        
        ans = ""

        while prev_idx > -1 or heap:
            while heap and heap[0][-1] <= prev_idx:
                heapq.heappop(heap)
            if heap and (prev_idx == -1 or heap[0][0] < s[prev_idx]):
                char, index = heapq.heappop(heap)
                ans += char
                visited.add(index)
                prev_idx = index - 1

            else:
                ans += s[prev_idx]
                visited.add(prev_idx)
                prev_idx -= 1
                
            while prev_idx in visited:
                prev_idx -= 1

        return ans