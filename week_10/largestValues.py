# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        parents = collections.deque([])
        children = collections.deque([])
        answer = []
        parents.append(root)
        while parents or children:
            temp = -float("inf")
            while parents:
                parent = parents.popleft()
                if parent == None:
                    continue
                temp = max(temp, parent.val)
                children.append(parent.left)
                children.append(parent.right)
            if temp != -float("inf"):
                answer.append(temp)
                temp = -float("inf")
            while children:
                child = children.popleft()

                if child != None:
                    parents.append(child)
        return answer