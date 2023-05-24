class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        what if we sort it by the type
        
        and for the type 3's if they are redundant at both remove them.
        how to check that they are redundant at both.
        
        try to find their parents in both cases and if the parents are equal in both cases remove them
        """
        count = 0
        parents = {1: [idx for idx in range(n + 1)], 2: [idx for idx in range(n + 1)]}
        rank = {1: [1] * (n + 1), 2: [1] * (n + 1)}
        edges.sort(key = lambda edge: edge[0], reverse = True)
        
        
        def find(node, type_):
            if node != parents[type_][node]:
                parents[type_][node] = find(parents[type_][node], type_)
                
            return parents[type_][node]
        
        
        def union(node1, node2, type_):
            parent1, parent2 = find(node1, type_), find(node2, type_)
            
            if parent1 == parent2:
                return True
            
            if rank[type_][parent2] > rank[type_][parent1]:
                parent1, parent2 = parent2, parent1
                
            parents[type_][parent2] = parent1
            rank[type_][parent1] += rank[type_][parent2]
            
            return False
        
        
        def valid(type_):
            unique = 0
            
            for node in range(1, len(parents[type_])):
                if node == find(parents[type_][node], type_):
                    unique += 1
            
            return unique == 1
        
        for type_, node1, node2 in edges:
            if type_ == 3:
                alice = union(node1, node2, 1)
                bob = union(node1, node2, 2)
                if alice and bob:
                    count += 1
            else:
                if union(node1, node2, type_):
                    count += 1
                    
                    
        validity = valid(1) and valid(2)
                
        return count if validity else -1