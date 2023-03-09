# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin, slow, fast = head, head, head

        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next

            if fast and slow == fast:
                while slow != begin:
                    slow = slow.next
                    begin = begin.next
                return slow
                
        return None
