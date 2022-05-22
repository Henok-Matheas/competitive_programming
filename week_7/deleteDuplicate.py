# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        begin = new

        while head != None:
            now = head
            prev = head
            while head and head.val == now.val:
                prev = head
                head = head.next
            if prev == now:
                new.next = ListNode(now.val)
                new = new.next
        return begin.next
