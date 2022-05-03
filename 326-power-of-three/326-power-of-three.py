class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n % 2: 
            return False
            
        while n >= 3 and n % 3 == 0:
            n //= 3
            
        return n == 1