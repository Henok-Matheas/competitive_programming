# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def validation(root):
            nonlocal isValid
            if not isValid:
                return
            elif not root:
                return None

            elif not root.left and not root.right:
                return root.val, root.val
            left = validation(root.left)
            right = validation(root.right)

            if not left and not right:
                return root.val, root.val

            if not left and right and root.val < min(right):
                return root.val, max(max(right), root.val)
            if not right and left and max(left) < root.val:
                return min(min(left), root.val), root.val

            if not left and right and root.val >= min(right):
                isValid = False
                return
            if not right and left and max(left) >= root.val:
                isValid = False
                return

            if left and right:
                print(left, right)
                if max(left) >= root.val or root.val >= min(right):
                    isValid = False
                    return

            return min(min(left), root.val), max(max(right), root.val)

        validation(root)
        return isValid
