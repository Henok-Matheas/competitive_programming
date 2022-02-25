# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        previous = None
        ans = 0

        while fast != None:
            fast = fast.next.next

            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp

        head1 = previous
        head2 = slow

        while head1 != None:
            ans = max(head1.val + head2.val, ans)
            head1 = head1.next
            head2 = head2.next
        return ans
