import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        whole = []

        for list in lists:
            while list != None:
                whole.append(list.val)
                list = list.next

        heapq.heapify(whole)

        node = ListNode(heapq.heappop(whole)) if whole else None
        if not node:
            return node
        begin = node

        n = len(whole)
        for index in range(n):
            node.next = ListNode(heapq.heappop(whole))
            node = node.next
        return begin
