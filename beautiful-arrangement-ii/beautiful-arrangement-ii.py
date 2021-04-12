class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        result = [num for num in range(1, n-k+1)]
        
        start = n - k + 1
        end = n
        while start < end:
            result.append(end)
            result.append(start)
            end -= 1
            start += 1
            
            
        if start == end:
            result.append(start)
            
        return result