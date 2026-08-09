from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        
    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft()) 
         
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
        
    def empty(self):
        return len(self.q) == 0

obj = MyStack()

obj.push(1)
obj.push(2)

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2, param_3, param_4)
