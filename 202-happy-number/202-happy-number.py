class Solution:
    def isHappy(self, n: int) -> bool:
        
        memo = set()
        
        def recursive(n: int) -> bool:
            if n == 1:
                return True
            
            if n in memo:
                return False
            
            memo.add(n)
            process = 0
            for num in map(int, str(n)):
                process += num ** 2
                
            return recursive(process)
        
        return recursive(n)
        