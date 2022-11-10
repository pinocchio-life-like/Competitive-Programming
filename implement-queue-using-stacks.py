class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x):
        while len(self.stk1) != 0:
            self.stk2.append(self.stk1[-1])
            self.stk1.pop()
 
        # Push item into self.s1
        self.stk1.append(x)
 
        # Push everything back to s1
        while len(self.stk2) != 0:
            self.stk1.append(self.stk2[-1])
            self.stk2.pop()
            
        

    def pop(self):
        if self.stk1:
            return self.stk1.pop()

    def peek(self):
        if self.stk1:
            return self.stk1[-1]

    def empty(self):
        return not self.stk1 and not self
