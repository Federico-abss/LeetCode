class Solution:
    def climbStairs(self, n: int) -> int:
        
        stairs = [1] + [0] * n
        step = 0
        
        while step < n:
            
            stairs[step+1] += stairs[step] 
            if step < n - 1:
                stairs[step+2] += stairs[step] 
                
            step += 1
            
        print(stairs)
        return stairs[-1]