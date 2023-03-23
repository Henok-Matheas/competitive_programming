class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
            
        
        
        parents = [idx for idx in range(n)]
        redundant = 0
        regions = n - 1
        for node1, node2 in connections:
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                ## same regions
                redundant += 1
            else:
                parents[parent1] = parent2
                regions -= 1
            
        print(regions, redundant, n)
        if redundant < regions:
            return -1
        
        return regions
                