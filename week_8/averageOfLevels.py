# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        parents = deque([])
        children = deque([])
        parents.append(root)
        answer = []

        while parents or children:
            sum = 0
            count = 0
            while parents:

                parent = parents.popleft()
                if parent:
                    sum += parent.val
                    count += 1
                if parent and parent.left:
                    children.append(parent.left)
                if parent and parent.right:
                    children.append(parent.right)
            answer.append(sum / count if count != 0 else 0)
            while children:
                child = children.popleft()
                if child:
                    parents.append(child)
        return answer
