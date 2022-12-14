# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        children = []
        answer = []
        
        while queue:
            length = len(queue)
            total = 0
            while queue:
                node = queue.pop()
                total += node.val
                
                if node.left:
                    children.append(node.left)
                    
                if node.right:
                    children.append(node.right)
                    
            answer.append(total / length)
                    
            while children:
                queue.append(children.pop())
                
        return answer