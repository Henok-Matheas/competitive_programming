# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        if not root 1 or root 2 return None
        
        if root1 but not root 2 return root1
        
        if root2 not root1 return root2
        
        if both
        
        return root with val = root1.val + root2.val
        """
        if not root2 and not root1:
            return None
        
        if root1 and not root2:
            return root1
        
        if root2 and not root1:
            return root2
        
        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        
        root1.val += root2.val
        
        root1.left = left
        root1.right = right
        
        return root1