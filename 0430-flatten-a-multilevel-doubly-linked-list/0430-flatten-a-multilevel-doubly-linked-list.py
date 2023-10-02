"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""

the recursion will return two things

the starting and the ending.


if the thing has a child:

do a recursion for the child:
which will return the head and tail


temp = curr.next
curr.next = recur_head
tail.next = temp

curr = temp
make the tail.next = node.next



the way to do it is

for the the recursion we need to pass


head
tail

node

while node:
    tail = node
    
    if node.child:
        temp_next = node.next
        recur_head, recur_tail = recur(node.child)
        node = temp_next
    
    node = node.next
  
  
return head, tail

    
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def recur(node):
            head = node
            tail = node
            
            while node:
                tail = node
                
                if node.child:
                    temp_next = node.next
                    recur_head, recur_tail = recur(node.child)
                    
                    node.next = recur_head
                    recur_head.prev = node
                    
                    recur_tail.next = temp_next
                    
                    if temp_next:
                        temp_next.prev = recur_tail
                    
                    
                    node.child = None
                    
                    node = recur_tail.prev
                    
                node = node.next
                
            return head, tail
        
        return recur(head)[0]
        