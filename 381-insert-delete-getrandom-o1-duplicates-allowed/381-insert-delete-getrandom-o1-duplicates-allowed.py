class RandomizedCollection:

    def __init__(self):
        self.set = defaultdict(list)
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            self.set[val].append(len(self.nums))
            self.nums.append(val)
            return False
        self.set[val].append(len(self.nums))
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        
        if self.nums[-1] == val:
            self.set[val].pop(self.set[val].index(len(self.nums)-1))
        else:
            idx = self.set[val].pop()
            lastVal = self.set[self.nums[-1]]
            lastVal.pop(lastVal.index(len(self.nums)-1))
            lastVal.append(idx)
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        if not self.set[val]:
            self.set.pop(val)
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return self.nums[randrange(len(self.nums))]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()