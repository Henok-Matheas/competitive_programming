#https://leetcode.com/problems/binary-tree-tilt/


#list approcch
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:
        # sum, tilt

        tilts = []

        def both(root):
            if not root:
                return [0, 0]
            if not root.left and not root.right:
                return [root.val, 0]

            sum = 0
            tilt = 0

            left = both(root.left)
            right = both(root.right)
            sum = left[0] + right[0] + root.val
            tilt = abs(left[0] - right[0])
            # tilts.append(tilt)

            tot_tilt = tilt + left[1] + right[1]
            # print("left",leftTup,"right",rightTup)
            # print("for root",root.val, "the sum tilt", tilt)

            return [sum, tot_tilt]

        return both(root)[1]
        # both(root)
        # return sum(tilts)


# sum of list approach


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:
        # sum, tilt

        tilts = []

        def both(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val

            sum = 0
            tilt = 0

            leftTup = both(root.left)
            rightTup = both(root.right)
            sum = leftTup + rightTup + root.val
            tilt = abs(leftTup - rightTup)
            tilts.append(tilt)

            # print("left",leftTup,"right",rightTup)
            # print("for root",root.val, "the sum tilt", tilt)

            return sum

        # return both(root)[1]
        both(root)
        return sum(tilts)
