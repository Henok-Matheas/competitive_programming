# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def addition(root, sum):
            if not root:
                return
            elif not root.left and not root.right:
                return sum + root.val == targetSum
            elif not root.left:
                return addition(root.right, sum + root.val)
            elif not root.right:
                addition(root.left, sum + root.val)
            return addition(root.left, sum + root.val) or addition(
                root.right, sum + root.val)

        return addition(root, 0)
