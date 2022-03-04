# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parents = collections.deque([])
        children = collections.deque([])

        level = 0

        if not root:
            return None

        parents.append([root, 0])

        answer = []
        answer.append([root.val])
        while parents or children:

            while parents:
                parent = parents.popleft()
                level = parent[1]

                if parent and parent[0].left:
                    children.append([parent[0].left, level + 1])
                if parent and parent[0].right:
                    children.append([parent[0].right, level + 1])

            temp = []
            while children:
                child = children.popleft()
                level = child[1]
                if child:
                    parents.append(child)
                    if level % 2 == 0:
                        temp.append(child[0].val)
                    else:
                        temp.insert(0, child[0].val)
            if temp:
                answer.append(temp)
        return answer
