class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        mod = target%2
        acc = idx = 0
        
        while acc < target or acc % 2 != mod:
            
            idx += 1
            acc += idx
            
        return idx
        
