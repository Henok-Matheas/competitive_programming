class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        sorted ancestors
        
        top sort question
        
        
        count the number of innodes for the ones who don't have innodes, add them to the queue
        
        while the queue exists
        
        pop from the queue
        
        for children of current
        ancestors[child].append(node)
        innode[child] -= 1
        
        if innnode is zero
        add to queue
        
        
        for every ancestor in ancestors:
        ancestors.sort()
        
        return ancestors
        """
        
        ancestors = [set() for _ in range(n)]
        ancestors_list = []
        innode = [0] * n
        parents = set([idx for idx in range(n)])
        children = {idx: set() for idx in range(n)}
        
        for start, end in edges:
            innode[end] += 1
            children[start].add(end)
            parents.discard(end)
              
        queue = deque(parents)
        
        
        while queue:
            node = queue.popleft()    
            
            for child in children[node]:
                innode[child] -= 1
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                
                if not innode[child]:
                    queue.append(child)
                    
        
        for ancestor in ancestors:
            ancestor_list = list(ancestor)
            ancestor_list.sort()
            ancestors_list.append(ancestor_list)
            
        return ancestors_list
                
                
            