class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        powers = [3 ** exp for exp in range(int(log(n, 3) + 1))]
       
        while n > 0:
            if not powers:
                return False
            idx = bisect_right(powers, n) - 1
            if idx < 0:
                return False
            power = powers.pop(idx)
            n -= power
            
            
        return n == 0