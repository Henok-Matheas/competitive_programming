# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        head => head.next
        
        temp = head.next
        prev = None
        
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
        
        head.next = head
        next.next = head
        head = next
        =>
        """
        prev = None
        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
            
        return prev