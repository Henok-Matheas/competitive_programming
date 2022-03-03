# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lefters = deque([])
        righters = deque([])
        
        lefters.append(root.left)
        righters.append(root.right)
        
        while lefters and righters:
            start = lefters.popleft()
            end = righters.popleft()
            
            if not start and not end:
                continue
            if start and end and start.val == end.val:
                lefters.append(start.left)
                lefters.append(end.left)
                righters.append(end.right)
                righters.append(start.right)
                continue
            else:
                return False
        return True