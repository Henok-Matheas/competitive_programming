# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        we just need to know the upper and lower limits and when we go left we lower the upper limit to curr val
        
        when we go right we increment the lower limit to the curr val
        
        let's do this using stack
        
        stack = [root]
        
        while stack
        curr
        
        if not lower <= curr.val <= upper:
        return False
        
        if left:
        
        """
        stack = [(root, -2 ** 31 - 1, 2 ** 31)]
        
        while stack:
            curr, lower, upper = stack.pop()
            
            if not lower < curr.val < upper:
                return False
            
            if curr.right:
                stack.append((curr.right, curr.val, upper))
            if curr.left:
                stack.append((curr.left, lower, curr.val))
        
        return True