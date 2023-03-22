class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        n cities
        roads = 
        
        not a heap instead we will be using a normal bfs to just track a path
        
        we can also use union find
        
        have parents list
        have rank list
        have also minimum list
        """
        
        parents = [idx for idx in range((n + 1))]
        rank = [1] * (n + 1)
        minimum = [float("inf")] * (n + 1)
        
        def find(node):
            if node == parents[node]:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2, distance):
            node1, node2 = find(node1), find(node2)
            
            if node1 == node2:
                minimum[node1] = min(minimum[node1], distance)
                
            else:
            ## rank
                parents[node2] = node1
                minimum[node1] = min(minimum[node1], distance, minimum[node2])
        
        for node1, node2, distance in roads:
            union(node1, node2, distance)
        
        return minimum[find(n)]
            