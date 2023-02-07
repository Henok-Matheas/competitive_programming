class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        n unique elems
        
        remember adjecent pairs [ui, vi]
        
        return original nums
        
        
        how to do that?
        
        one approach start from the motherfuckers from the ones with one connection
        
        you have n - 1 connections
        
        """
        order = []
        graph = defaultdict(set)
        
        for node1, node2 in adjacentPairs:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
            
        current = None
        
        for node in graph:
            if len(graph[node]) == 1:
                current = node
        
        while current is not None:
            order.append(current)
            
            if not graph[current]:
                return order
                
            neigh = graph[current].pop()

            graph[neigh].discard(current)

            current = neigh
                
        return order