class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addValueAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addValueAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addValueAtAnyIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addValueAtHead(val)
        elif index == self.size:
            self.addValueAtTail(val)
        else:
            new_node = Node(val)
            prev, curr = None, self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            prev.next = new_node
            new_node.next = curr
            self.size += 1

    def deleteValueAtAnyIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev, curr = None, self.head
            for _ in range(index):
                prev = curr
                curr = curr.next
            prev.next = curr.next
        self.size -= 1






