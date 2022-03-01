# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:

        g_parent = None

        total = []

        if not root.left and not root.right:
            return 0

        def checker(root, parent, grand):
            if not root:
                return
            # elif not root.left and not root.right:
            #     if grand % 2 == 0:
            #         total.append(root.val)
            #     return

            if grand and grand.val % 2 == 0:
                total.append(root.val)

            checker(root.left, root, parent)
            checker(root.right, root, parent)

        checker(root.left, root, None)
        checker(root.right, root, None)

        value = 0
        for root in total:
            value += root

        return value
