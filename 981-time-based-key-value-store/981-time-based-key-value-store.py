class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.keys[key]
        idx = self.binarySearch(values, timestamp)
        if not values or values[0][1] > timestamp:
            return ""
        return values[idx][0]
        
        
    def binarySearch(self, pairs, target) -> int:
        
        l = 0
        r = len(pairs)
        while l < r:
            mid = l + (r-l) // 2
            midVal = pairs[mid][1]
            if midVal == target:
                return mid
            elif midVal > target:
                r = mid
            else:
                l = mid+1
                
        return l-1
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)