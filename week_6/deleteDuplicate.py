# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        count = 0
        final = head
        while head != None and head.next != None:
            if head.val == head.next.val:
                temp = head.next
                head.next = head.next.next
                temp.next = None
                if count == 0:
                    final = head
            else:
                head = head.next
                count += 1
        return final
                
            
        