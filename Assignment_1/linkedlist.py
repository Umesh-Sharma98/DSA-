class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")



    # for example
    #list = Sll()
    # list.insert(0,10)
    # list.insert(1,15)


    # list.insert(2,20) 

    # list.insert(1,40)
    # list.print_list()



    #que 2 :- Delete at any specific index  
    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

    # list = Sll()
    # list.insert(0,10)
    # list.insert(1,15)
    # list.insert(2,20)
    # list.insert(3,25)

    # list.print_list()

    # list.delete(2)
    # list.print_list()
    # list.delete(2)
    # list.print_list()
    

    #que 3 :- get the size of linkedlist  



    def get_size(self):
        return self.size
    
    # list = Sll()
    # list.insert(0,10)
    # list.insert(1,15)
    # list.insert(2,20)
    # list.insert(3,25)
    # list.insert(4,40)

    # print("Size:", list.get_size())

    # que 4 :- check to the empty linked list 

    def is_empty(self):
        return self.size == 0
    
    # list  = Sll()
    # list.insert(0,10)
    # list.delete(0)
    # print(list.is_empty())

    # que 5 :- rotate at k 


    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        if k == 0:
            return
        curr = self.head
        length = 1

        while curr.next:
            curr = curr.next
            length += 1
        curr.next = self.head  # Form a circular linked list

        steps_new_head = length - k
        new_tail = self.head
        for _ in range(steps_new_head - 1):
            new_tail = new_tail.next
        self.head = new_tail.next
        new_tail.next = None


    # que 6 :-  reverse the linked list 

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # que 7 :- append at the end 


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    #que 8 :- prepend element at the beggining of linked list 

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1



     #que 9 :-  merge two linked list 

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = other_list.head
        self.size += other_list.size


    #que 10 :- 


    #que 11:- find the middle element 


    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


    #que 12:- first occurance of element 

    def index_of(self, data):
        curr = self.head
        index = 0
        while curr:
            if curr.data == data:
                return index
        curr = curr.next
        index += 1
        return -1



    #que 13 : - split linked in two linked list at any specific index 


    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        if index == 0:
            new_list = Sll()
            new_list.head = self.head
            self.head = None
            new_list.size = self.size
            self.size = 0
            return new_list
        curr = self.head
        for i in range(index - 1):
            curr = curr.next
            new_list = Sll()
            new_list.head = curr.next
            new_list.size = self.size - index
            self.size = index
            curr.next = None
            return new_list 
