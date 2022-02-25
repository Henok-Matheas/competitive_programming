# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        begin = head
        final = head

        while head != None:
            lst.append(head.val)
            head = head.next

        lst.sort()

        for num in lst:
            begin.val = num
            begin = begin.next

        return final
