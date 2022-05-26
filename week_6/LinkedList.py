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
        counter = 0
        curr = self.head
        while counter < index:
            curr = curr.next
            counter += 1
        return curr.value if curr and counter == index else -1

    def addAtHead(self, val: int) -> None:
        node = Linked(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        node = Linked(val)
        if self.length == 0:
            self.addAtHead(val)
            return
        while curr and curr.next:
            curr = curr.next
        curr.next = node
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

        counter = 0
        curr = self.head
        node = Linked(val)
        while counter < index - 1:
            curr = curr.next
            counter += 1
        node.next = curr.next
        curr.next = node
        self.length += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length or self.head == None:
            return

        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return

        counter = 0
        curr = self.head

        while counter < index - 1:
            curr = curr.next
            counter += 1

        temp = curr.next
        curr.next = curr.next.next
        temp.next = None
        self.length -= 1
        return

    def iterate(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next