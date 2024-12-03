# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        simplest = have a new linked list
        
        head = ListNone()
        ans = head
        
        if not l1 or l2:
        return
        
        while l1 or l2:
        if l1 and l2 and l1 lower or (l1 and not l2):
        head.val = l1.val
        l1 = l1.next
        
        if l1 and l2 and l2 lower:
        head.val = l2.val
        l2 = l2.next
        
        if l1
        
        head.next = ListNone()
        head = head.next
        """
        if not list1 and not list2:
            return None
        head = ListNode()
        ans = head
        
        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val or (list1 and not list2):
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next
        
        return ans.next
        
        