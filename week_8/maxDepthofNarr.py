"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def depth(self, root, depth):
        if root == None or root.children == None:
            return depth
        maxim = 0
        for child in root.children:
            maxim = max(maxim, self.depth(child, depth + 1))
        return max(maxim, depth + 1)

    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root, 0)
