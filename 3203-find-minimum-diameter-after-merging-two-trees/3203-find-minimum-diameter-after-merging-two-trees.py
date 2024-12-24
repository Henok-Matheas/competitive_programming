class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        """
        this is just topSort which will give us the diameters of the two trees
        
        when we connect them
        
        if both length are equal then answer is len1 + len2 + 1
        
        one edge case-ish is when the diameter exists within a single tree
        
        meaning when two of it's children have very long paths whose sum is larger than len1 + len2
        
        so to handle this when traversing using topSort
        we do maxim = max(maxim, the current depth + max_depth[parent_node])
        
        
        STEPS:
        1. CREATE THE TREES USING A LIST STRUCTURE
        2. GO OVER THE LIST AND CHOOSE ONES WHOSE LEN(CHILDREN) IS == 1 AND ADD TO QUEUE
        3. POP FROM QUEUE = NODE, CURR_LENGTH
        4. GO OVER CHILDREN
            - MAXIM = MAX(MAXIM, CURR_LENGTH + 1 + MAX_DEPTH[CHILD])
            - MAX_DEPTH[CHILD] = MAX(MAX_DEPTH[CHILD], CURR_LENGTH + 1)
            - IF LEN(CHILDREN[CHILD]) == 1:
                - ADD TO QUEUE
        5. RETURN MAX_DEPTH, MAXIM
        6. LET 1 - 5 BE A FUNCTION WHICH TAKES IN THE EDGES LIST
        7. CALL THE FUNC FOR TREE1 AND TREE2
        8. RETURN MAX(MAX_DEPTH1 + MAX_DETPH2 + 1, MAXIM1, MAXIM2)
        """
        def calcDepth(edges: List[List[int]]):
            N = len(edges) + 1
            graph = [set([]) for _ in range(N)]
            depths = [0] * N
            
            for node1, node2 in edges:
                graph[node1].add(node2)
                graph[node2].add(node1)
                
            queue = deque([])
            max_depth, max_diameter = 0, 0
            
            for node in range(N):
                if len(graph[node]) == 1:
                    level = 0
                    queue.append([node, level])
                    
            while queue:
                node, level = queue.popleft()
                
                if len(graph[node]):
                    child = graph[node].pop()
                    max_diameter = max(max_diameter, level + 1 + depths[child])
                    depths[child] = max(depths[child], level + 1)
                    max_depth = max(max_depth, depths[child])
                    
                    graph[child].remove(node)
                    
                    if len(graph[child]) == 1:
                        queue.append([child, level + 1])
              
            return max_depth, max_diameter
        
        depth1, diameter1 = calcDepth(edges1)
        depth2, diameter2 = calcDepth(edges2)
        
        return max(diameter1, diameter2, depth1 + depth2 + 1)
            