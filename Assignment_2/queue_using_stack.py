from collections import deque 

class Queue:

    def __init__(self):
        self.stack1 = deque() 
        self.stack2 = deque()  

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def transfer(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        if not self.stack2:
            self.transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            self.transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        


