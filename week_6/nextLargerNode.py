# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        mono_stack = []
        
        final = []
        count = 0
        
        while head != None:
            while mono_stack and mono_stack[-1][1] < head.val:
                final[mono_stack.pop()[0]] = head.val
            mono_stack.append([count,head.val])
            final.append(0)
            head = head.next
            count += 1
        return final
        