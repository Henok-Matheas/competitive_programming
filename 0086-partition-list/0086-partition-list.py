# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        place holder seeker two pointer solution
        
        while seeker:
        if seeker.val < x:
            place.val, seeker.val = seeker.val, place.val
            place = place.next
        seeker = seeker.next
        
        gather the lower at one place, the higher at one place
        
        then merge them
        
        """
        low = ListNode()
        high = ListNode()
        high_s = high
        ans = low
        
        while head:
            if head.val < x:
                low.next = head
                low = head
                head = head.next
                low.next = None
            else:
                high.next = head
                high = head
                head = head.next
                high.next = None
            
        low.next = high_s.next
            
        return ans.next