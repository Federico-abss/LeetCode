class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []
        
​
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minimum == []:
            self.minimum.append(x)
        elif x <= self.getMin():
            self.minimum.append(x)
        
​
    def pop(self) -> None:
        if self.getMin() == self.stack.pop():
            self.minimum.pop()
        
​
    def top(self) -> int:
        return self.stack[-1]
        
​
    def getMin(self) -> int:
        return self.minimum[-1]
        
​
​
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
