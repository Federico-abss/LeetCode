class Solution:
    def countArrangement(self, n: int) -> int:
        
        seen = {}
        arr = []
        result = 0
        
        def isBeutiful(num, idx):
            
            return not num % idx or not idx % num 
        
        def helper():
            nonlocal result            
            
            if len(arr) == n:
                result += 1
                return 
            
            for num in range(1, n + 1):
            
                if num not in seen and isBeutiful(num, len(arr) + 1):
                    arr.append(num)
                    seen[num] = "#"
                    helper()
                    seen.popitem()
                    arr.pop()
        
        helper()
        return result
            
            
            
