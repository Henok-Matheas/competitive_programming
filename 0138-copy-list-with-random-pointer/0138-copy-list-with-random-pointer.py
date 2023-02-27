"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        begin = Node(head.val)
        visited = {head: begin, None: None}
        while head:
            new = visited[head]
            if head.random:
                if head.random not in visited:
                    visited[head.random] = Node(head.random.val)
                new.random = visited[head.random]
            if head.next not in visited:
                visited[head.next] = Node(head.next.val)
            new.next = visited[head.next]
            head = head.next
        
        return begin