def myPowNaive(x: float, n: int):
    if n == 0:
        return 1
    
    result = x
    while n > 1:
        result *= x
        n -= 1
            
    return result
    

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        target = floor(sqrt(n))
        remainder = n - target * target

        result = myPowNaive(x, target)
        result = myPowNaive(result, target)
        result *= myPowNaive(x, remainder)

        return result
    

        