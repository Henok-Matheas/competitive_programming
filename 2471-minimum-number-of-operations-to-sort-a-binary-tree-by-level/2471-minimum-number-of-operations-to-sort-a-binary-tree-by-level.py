# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        so we find their levels and then go level by level
        then compare the unsorted with the sorted and count how many need to be changed and then do count - 1
        
        PSEUDO
        
        DFS(LEVEL, NODE):
        append to an array at level
        
        
        for level:
        count = -1
        sorted_level = sort()
        for nodes in level:
        if sorted_level[idx]  != node:
        count += 1
        
        total += max(0, count)
        
        return total
        
        so now we will just do a swapper function
        
        how to do the swapper function?
        
        have a sorted
        have a dictionary of their positions
        
        for idx, val in sorted_levels:
        if idx != positions[val]:
            count += 1
            positions[levels[idx]] = positions[val]
            positions[val] = idx
            
        49
        45                  1
        20            46
        15      39    25
        27 N    N  N
        
        
        so we just need to find circular regions then find their sizes and do size - 1
        
        actual_positions = 
        graph = {idx : actual_positions[val]}
        
        
        traverse(idx):
            if levels[idx] < 0:
                return -1
            levels[idx] = -1
            return 1 + traverse(graph[idx])
        for idx in range(n):
            if levels[idx] != -1:
                total += traverse(idx)
        
        
        """
        levels = []
        total = 0
        
        def traverse(idx, graph, level):
            if level[idx] == -1:
                return -1
            level[idx] = -1
            return 1 + traverse(graph[idx], graph, level)
        
        
        def swapCount(level):
            count = 0
            sorted_level = list(sorted(level))
            actual_positions = {val : idx for idx, val in enumerate(sorted_level)}
            graph = {idx : actual_positions[val] for idx, val in enumerate(level)}
            
            for idx, val in enumerate(level):
                if level[idx] != -1:
                    count += traverse(idx, graph, level)
            return count
        
        def dfs(level, node):
            if not node:
                return 0
            
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            
            return 1 + max(dfs(level + 1, node.left), dfs(level + 1, node.right))
        
        max_level = dfs(0, root)
        # print(levels)
        for level in levels:
            total += swapCount(level)
            
        return total