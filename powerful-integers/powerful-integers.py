class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        if x == y == 1 and bound >= 2:
            return [2]
        
        result = set()
        for n in range(int(sqrt(bound))+1):
            for m in range(int(sqrt(bound))+1):
                
                powInt = pow(x, m) + pow(y, n)
                if powInt > bound:
                    break
                result.add(powInt)
                
        return result