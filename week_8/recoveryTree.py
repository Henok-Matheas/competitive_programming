# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        output = None
        first = None
        second = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            rt = stack.pop()
            if output and output.val >= rt.val and first == None:
                first = output
            if output and output.val >= rt.val and first != None:
                second = rt
            output = rt
            root = rt.right
        first.val, second.val = second.val, first.val

        # print(output)


#         now = output[-1] if output != None else None
#         prev = None
#         i = len(output) - 2
#         while i > -1:
#             prev = output[i]
#             if prev.val >= now.val and second == None:
#                 second = now
#                 break
#             now = prev
#             i -= 1

#         curr = output[0] if output != None else None
#         nex = None
#         i = 1
#         while i < len(output):
#             nex = output[i]
#             if nex.val <= curr.val and first == None:
#                 first = curr
#                 break
#             curr = nex
#             i += 1

#         first.val, second.val = second.val, first.val
