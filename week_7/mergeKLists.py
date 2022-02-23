import heapq


# Definition for singly-linked list.
class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:

    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        l_list = []

        for node in lists:
            if node:
                heapq.heappush(l_list, Node(node.val, node.next))
        merged = Node("")
        if l_list:
            node = heapq.heappop(l_list)
            merged = Node(node.val)
            node = node.next
            if node:
                heapq.heappush(l_list, Node(node.val, node.next))

        merger = merged

        while l_list:
            node = heapq.heappop(l_list)
            merged.next = Node(node.val)
            merged = merged.next
            node = node.next
            if node:
                heapq.heappush(l_list, Node(node.val, node.next))

        return merger


# import heapq
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:

#     def mergeKLists(self,
#                     lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         whole = []

#         for list in lists:
#             while list != None:
#                 whole.append(list.val)
#                 list = list.next

#         heapq.heapify(whole)

#         node = ListNode(heapq.heappop(whole)) if whole else None
#         if not node:
#             return node
#         begin = node

#         n = len(whole)
#         for index in range(n):
#             node.next = ListNode(heapq.heappop(whole))
#             node = node.next
#         return begin
