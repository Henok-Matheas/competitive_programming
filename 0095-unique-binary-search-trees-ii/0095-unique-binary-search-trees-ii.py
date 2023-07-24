# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        
        what if I start from all the nodes and have a visited set
        then for every node not in visited we can randomly make it the next node to be insterted.
        finally when every node has been inserted we can have a function that will deserialize it/ make it into a list format
        
        
        problem: will this not TLE?
        answer: it will pass
        
        
        problem: will it only generate the unique BSTs?
        answer: NO
        
        solution: what if the state reflected the individuality, meaning what if we had a representation for the BST in some way?
        representation: have a tuple, and in the tuples we will either have 0, or level - (left / right)
        
        
        
        current solution:
        
        backtrack(bst, visited):
        if all are filled:
            answer.append(desirialize(bst))
            
        
        
        
        
        depth is n, branching factor is n
        
        
        n ** n
        
        8 ** 8
        
        problem: I can't just use the most recent one.
        solution: 
        
        problem: how to place on left and right
        problem: how to traverse
        
        
        for the state we can have the array having 
        
        
        deserialize
        
        if the current level is node_dict
            return none
    
        node = Node(node_dict[level])
        
        
        
        node.left = deserialize(level + "L")
        node.right = deserialize(level + "R")
        
        return node
        
        """
        
        def deserialize(level, node_dict):
            if level not in node_dict:
                return None
            
            node = TreeNode(node_dict[level] + 1)
            
            node.left = deserialize(level + "L", node_dict)
            node.right = deserialize(level + "R", node_dict)
            
            return node
        
        
        def delete(node, array, node_dict, visited):
            level = array[node]
            node_dict.pop(level)
            array[node] = 0
            
        
        def insert(level, node, array, node_dict, visited):
            if level not in node_dict:
                node_dict[level] = node
                array[node] = level
                return 
            
            if node < node_dict[level]:
                insert(level + "L", node, array, node_dict, visited)
                
            else:
                insert(level + "R", node, array, node_dict, visited)
                
        
        def mutate(array):
            return tuple(array)
        
        
        def backtrack(array, node_dict, visited, visited_state):
            state = mutate(array)
            
            if state in visited_state:
                return
            
            visited_state.add(state)
            
            if len(visited) == n:
                bst = deserialize("F", node_dict)
                answer.append(bst)
                return
            
            
            
            for node in range(n):
                if node not in visited:
                    insert("F", node, array, node_dict, visited)
                    visited.add(node)
                    backtrack(array, node_dict, visited, visited_state)
                    visited.remove(node)
                    delete(node, array, node_dict, visited)
                
                
                
        array = [0] * n
        node_dict = {}
        visited = set()
        visited_state = set()
        answer = []
        
        backtrack(array, node_dict, visited, visited_state)
        return answer
            
            
        
        
        