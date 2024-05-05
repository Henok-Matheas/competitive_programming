# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        we will have node and next
        
        node.val = next.val
        node = node.next
        next = next.next
        
        finally we will make node.next = none
        
        
        we will never be given the last node so it works
        """
        next_ = node.next
        
        while node:
            node.val = next_.val
            next_ = next_.next
            if not next_:
                node.next = None
            node = node.next
            
        