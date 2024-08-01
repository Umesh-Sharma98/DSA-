class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def _init_(self, capacity) -> Node: 
        self.capacity = capacity
        self.cache = {}  
        self.head = Node(0, 0)  
        self.tail = Node(0, 0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node
        
        if len(self.cache) > self.capacity:
            tail_node = self.tail.prev
            self._remove(tail_node)
            del self.cache[tail_node.key]