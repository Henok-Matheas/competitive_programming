# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertionSortList(self,
                          head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(head):
            while head.next and head.val > head.next.val:
                head.val, head.next.val = head.next.val, head.val
                head = head.next

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            rev(head)
            head = temp
        return prev
