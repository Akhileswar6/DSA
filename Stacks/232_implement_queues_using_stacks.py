class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
       

    def push(self, x):
        self.inStack.append(x)
        

    def pop(self):
        self.peek()
        return self.outStack.pop()
        

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        return not self.inStack and not self.outStack


obj = MyQueue()
obj.push(1) 
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())