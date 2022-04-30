class RandomizedSet:

    def __init__(self):
        self.set = dict()
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        idx = self.set[val]
        self.set[self.nums[-1]] = idx 
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.set.pop(val)
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return self.nums[randrange(len(self.nums))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

