# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = 2
        prev_head = ListNode(0, None)
        begin = head
        cnt = 0

        while head:
            starting = head
            count = 0

            while count < k and head != None:
                head = head.next
                count += 1
            previous = None
            if count == k:
                head = starting
                #this means we can reverse
                for i in range(k):
                    temp = head.next
                    head.next = previous
                    previous = head
                    head = temp

            if cnt < 1:
                begin = previous if previous else starting
                cnt += 1
            prev_head.next = previous if previous != None else starting
            prev_head = starting
        return begin
