class MinStack:

    def __init__(self):
        self.q = []
        self.stack = []
        

    def push(self, val: int) -> None:
        heappush(self.q, val)
        self.stack.append(val)
        

    def pop(self) -> None:
        removed = self.stack.pop()
        self.q.pop(self.q.index(removed))
        heapify(self.q)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.q[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()