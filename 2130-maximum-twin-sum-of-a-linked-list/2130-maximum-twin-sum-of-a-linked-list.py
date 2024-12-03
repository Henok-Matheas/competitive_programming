# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        this requires the turtle and hare algorithm for reversing/ palindroming
        """
        slow, fast = head, head
        prev = None
        maxim = 0
        
        while fast and fast.next:
            fast = fast.next.next
            
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_
            
        head1, head2 = prev, slow if fast == None else slow.next
        
        while head2:
            maxim = max(maxim, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
            
        return maxim