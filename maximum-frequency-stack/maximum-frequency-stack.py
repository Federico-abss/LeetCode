class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(list)
        self.nodes = defaultdict(int)
        self.maxFreq = 0
        

    def push(self, x: int) -> None:
        self.nodes[x] += 1
        amount = self.nodes[x]
        self.frequency[amount].append(x)
        self.maxFreq = max(amount, self.maxFreq)
        

    def pop(self) -> int:
        numToRemove = self.frequency[self.maxFreq].pop()
        if not self.frequency[self.maxFreq]:
            self.maxFreq -= 1
        self.nodes[numToRemove] -= 1
        return numToRemove


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()