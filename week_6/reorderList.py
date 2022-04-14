# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        begin = head
        fast = head
        slow = head
        bef = None

        while head.next and fast and fast.next != None:
            fast = fast.next.next
            bef = slow
            slow = slow.next

        if fast == slow:
            return

        bef.next = None

        header = head
        tailer = slow

        previous = None
        while tailer:
            temp = tailer.next
            tailer.next = previous
            previous = tailer
            tailer = temp

        tailer = previous
        # print("this is tailer",tailer)
        count = 0
        while header != None and tailer != None:
            if count % 2 == 0:
                temp = header.next
                header.next = tailer
                header = temp
            else:
                temp = tailer.next
                tailer.next = header
                tailer = temp
            count += 1
        return begin
