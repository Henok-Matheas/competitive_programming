# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0

        head = ListNode(0)
        begin = head

        while l1 or l2 or extra != 0:
            first = l1.val if l1 != None else 0
            second = l2.val if l2 != None else 0
            total = first + second + extra
            final = total % 10
            extra = total // 10
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            head.next = ListNode(final)
            head = head.next
        return begin.next
