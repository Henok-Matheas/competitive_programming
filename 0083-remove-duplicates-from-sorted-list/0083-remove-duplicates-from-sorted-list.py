# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        seeker, placeholder?
        we need head and prev
        
        if head.val == prev.val:
        seeker.next = None
        else
        seeker.next = head
        seeker = head
        """
        seeker = head
        ans = seeker
        
        while head and head.next:
            curr = head.next
            prev = head
            
            if curr.val == prev.val:
                head = head.next
                seeker.next = None
            else:
                seeker.next = curr
                seeker = seeker.next
                head = head.next
        
        return ans