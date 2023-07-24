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
        
        
        while representing it, you can wait until the end.
        
        """
        
        """
        
        second way
        
        what if I had a function which returned the list of bsts from some start to an end, then we can make it a divide and conquer question
        
        for a single node
        
        trees(1, 1)
        return [Node(1)]
        
        trees(1, 2)
        answer = []
            for node in range(start, end + 1):
                for left in trees(start, node) or [None]:
                    for right in trees(node + 1, end + 1) or [None]:
                        answer.append(TreeNode(node, left, right))
                        
            return answer
                
        
        """
        
        def trees(start, end):
            return [TreeNode(node, left, right) for node in range(start, end + 1) for left in trees(start, node - 1) for right in trees(node + 1, end)] or [None]
        
        return trees(1, n)
            
            
        
        
        