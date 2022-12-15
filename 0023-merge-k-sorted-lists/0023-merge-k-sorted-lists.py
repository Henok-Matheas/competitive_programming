# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __gt__(self, other):
        return self.val >= other.val
    
    def __lt__(self, other):
        return self.val <= other.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final = ListNode(0)
        head = final
        
        heap = []
        
        for node in lists:
            if node:
                heapq.heappush(heap, ListNode(node.val,node.next))
                
        while heap:
            node = heapq.heappop(heap)
            head.next = ListNode(node.val)
            head = head.next
            
            node = node.next
            
            if node:
                heapq.heappush(heap, ListNode(node.val,node.next))
        
        
        
        return final.next