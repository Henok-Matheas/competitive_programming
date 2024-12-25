# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def dfs(node, level):
            if not node:
                return
            if level == len(answer):
                answer.append(node.val)
            answer[level] = max(answer[level], node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
        return answer