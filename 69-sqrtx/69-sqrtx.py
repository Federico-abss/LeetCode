class Solution:
    def mySqrt(self, x: int) -> int:
        
        if not x: return x
        
        candidate = 2
        prev = 1
        
        while candidate ** 2 < x:
            prev = candidate
            candidate **= 2
            
        candidate = prev << 1
            
        while candidate ** 2 < x:
            prev = candidate 
            candidate <<= 1
            
        candidate = prev
            
        while candidate ** 2 < x:
            candidate += 1
            
        return candidate if candidate ** 2 == x else candidate -1
            
            