# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = []
        answer = []

        def traversal(node, row, col):
            if not node:
                return None

            positions.append([col, row, node.val])

            traversal(node.left, row + 1, col - 1)
            traversal(node.right, row + 1, col + 1)

        traversal(root, 0, 0)
        
        positions.sort()

        for idx, (col, row, value) in enumerate(positions):
            if not idx or col != positions[idx - 1][0]:
                answer.append([])

            answer[-1].append(value)

        return answer
        ## sort the dictionary

