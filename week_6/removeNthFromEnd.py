# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        begin = head
        slow = head
        fast = head
        
        count = 0
        tmp = head
        
        while tmp != None:
            count += 1
            tmp = tmp.next
            
            
        
        cnt = n
        
        while cnt > 0:
            fast = fast.next
            cnt -= 1
        print("count",count)
        if count == n:
            if count == 1:
                return None
            slow.val, slow.next.val = slow.next.val, slow.val            
            temp = slow.next
            slow.next = slow.next.next
            temp.next = None
            return slow
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = slow.next.next
        temp.next = None
        
        return begin
        