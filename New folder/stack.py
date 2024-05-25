class node: 
    def __init__(self,data, next = None):
        self.data = data 
        self.next = next


class stack : 
    def __init__(self):
        self.size = 0
        self.head = None 



    def size(self) -> int :
        return self.size   

    def isempty (self) -> bool:
        return (self.size() == 0)
    
    def push(self,val):
        newNode = node(val,head)
        head = newNode 
        self.size +=1

    

    def pop(self): # return top element and remve it 
        if self.isempty():
            raise Exception ("stack overflow ")
        

        data = self.head.data 
        temp = self.head
        self.head = self.head.next
        del temp 
        self.size -=1 


    def top(self):
        if self.isempty():
            raise Exception ("stack underflow ")
        return self.head.data
    
    def __str__(self) -> str:
        st = [ ]
        trav = self.head 
        while trav :
            st.append(str(trav.data))
            trav = trav.next

            return '-> '(s)
