# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        linked = ListNode(None,None)
        
        final = linked
        while list1 != None or list2 != None:
            print("got in")
            if (list1 != None and list2 == None) or (list1 != None and (list1.val  <= list2.val)):
                
                linked.next = list1
                list1 = list1.next
                linked = linked.next
            elif (list2 != None and list1 == None) or (list2 != None and (list2.val  < list1.val)):
                linked.next = list2
                list2 = list2.next
                linked = linked.next
                
        return final.next
            
        