class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
     
        res = 0
        count = 1
        for num in arr:
            
            while num != count:    
                
                k -= 1
                if not k:
                    return count
                count += 1
            
            count += 1
        
        while k:
            
            count += 1
            k -= 1
            
        return count - 1
            
            
