# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer= []
        queue = deque([])
        if root:
            order = 0
            queue.append([root, order])            
            
        while queue:
            node, order = queue.popleft()
            
            if order == len(answer):
                answer.append([])
                
            answer[-1].append(node.val)
            
            if node.left:
                queue.append([node.left, order + 1])
            
            if node.right:
                queue.append([node.right, order + 1])
        
        return answer