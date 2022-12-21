# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        def builder(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if not inorder or not postorder:
                return None
            current = postorder[0]
            finder = inorder.index(current)

            root = TreeNode(current)
            
            post_index = len(postorder) - finder


            root.left = builder(inorder[: finder], postorder[post_index: ])
            root.right = builder(inorder[finder + 1:], postorder[1 : post_index])
            
            return root
        
        
        
        return builder(inorder, postorder[::-1])
        