class ChainNode:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class SeparateChainingUsingHashMap:
    def _init_(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity 

    def _hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return True
            current = current.next

        return False

    def insert(self, key, value):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = ChainNode(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next


            