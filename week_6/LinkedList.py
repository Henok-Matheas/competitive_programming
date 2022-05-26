class Linked:

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        curr = self.head
        while index and curr:
            curr = curr.next
            index -= 1
        return curr.value if curr else -1

    def addAtHead(self, val: int) -> None:
        node = Linked(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        node = Linked(val)
        while curr and curr.next:
            curr = curr.next

        if curr:
            curr.next = node
        else:
            self.addAtHead(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index > self.length:
            return

        curr = self.head
        node = Linked(val)
        while index - 1:
            curr = curr.next
            index -= 1
        node.next = curr.next
        curr.next = node
        self.length += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length or self.head == None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        while index - 1:
            curr = curr.next
            index -= 1

        curr.next = curr.next.next
        self.length -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)