class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next_ = None
class LRUCache:
    """
    you have a cache of size capacity
    get(key): returns value of key
    put(key, value): update value with value or create a new node with value
    
    whenever the two methods are called we move the nodes to the new part
    
    first approach
    
    get()
    have a dict of key to nodes as well
    have a linkedlist of nodes(key, value)
    if it exists
    key, value = node
    call put(key, value)
    else:
    -1
    
    
    for put():
    if it exists:
    delete()
    add it to the new place
    if it doesn't exist:
    add to newplace
    
    
    add(key, value)
    
    create a node()
    
    if the size == n
    make next of head = head.next.next
    head.next.next.prev = head
    node()
    
    prev = tail.prev
    prev.next = node
    tail.prev = node
    node.next = tail
    node.prev = tail
    
    
    
    delete():
    next = node.next 
    prev = node.prev
    prev.next = next
    next.prev = prev
    size -= 1
    """

    def __init__(self, capacity: int):
        self.size = 0
        self.CAP = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next_ = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        value = self.nodes[key].value
        self.put(key, value)
        return value
    
    
    def delete(self, key):
        node = self.nodes.pop(key)
        
        prev, next_ = node.prev, node.next_
        prev.next_, next_.prev = next_, prev
        self.size -= 1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.delete(key)
            
        if self.size == self.CAP:
            self.delete((self.head).next_.key)
        node = Node(key, value)
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next_ = self.tail
        prev_node.next_ = node
        self.tail.prev = node
        self.nodes[key] = node
        self.size += 1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)