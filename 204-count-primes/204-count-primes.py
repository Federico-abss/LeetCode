class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes = [1] * n
        primes[0:2] = [0,0]
        
        for idx in range(2,int(n ** 0.5) + 1):
            if primes[idx]:
                primes[idx**2:n:idx] = [0] * len(primes[idx**2:n:idx])
        
        return sum(primes)