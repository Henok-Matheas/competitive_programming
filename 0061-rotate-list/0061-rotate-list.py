# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        connect the head to the tail and then make the k-1 node's next None and then return the kth node as the head
        
        ## first round we use to count total and connect the tail to the head
        
        ## second round we use to reach total - k and make that the head and also make the prev.next = None
        ## to do that we do a while total - k - 1 >= 0
        curr = curr.next
        
        next_ = curr.next
        curr.next = None
        return next_
        """
        if not head:
            return head
        
        total, curr = 1, head
        while curr.next:
            total += 1
            curr = curr.next    
        curr.next = head
        
        k %= total
        for _ in range(total - k - 1):
            head = head.next
            
        next_ = head.next
        head.next = None
        
        return next_
        
        