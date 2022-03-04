# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def lowest(root):
            if not root:
                return None

            if not root.left and not root.right:
                return 1, "leaf", root

            # for non-leaft
            left = None
            right = None
            if root.left:
                left = lowest(root.left)
            if root.right:
                right = lowest(root.right)

            if left and left[1] == "leaf" and right and right[1] == "leaf":
                # print("both leafs",root.val)
                return left[0] + 1, "nonleaf", root

            # working with branches atleast one of which is non-leaf

            val = None
            length = 0
            if left and right:
                if left[0] > right[0]:
                    val = left[2]
                    length = left[0] + 1
                elif right[0] > left[0]:
                    length = right[0] + 1
                    val = right[2]
                elif right[0] == left[0]:
                    length = left[0] + 1
                    val = root
            elif left:
                val = left[2]
                length = left[0] + 1
            elif right:
                val = right[2]
                length = right[0] + 1
            return length, "nonleaf", val

        value = lowest(root)
        # print(value)
        return value[2]
