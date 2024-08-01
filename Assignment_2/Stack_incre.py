class Stack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []      
        self.incre = []  

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incre.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        inc = self.incre[idx]
        if idx > 0:
            self.incre[idx - 1] += inc
        val = self.stack.pop() + inc
        self.incre.pop()
        return val

    def incre(self, k: int, val: int) -> None:
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.incre[idx] += val

        



