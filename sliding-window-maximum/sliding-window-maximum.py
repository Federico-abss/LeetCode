class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def increaseDQ(num, idx):
            
            if dq and num >= dq[0][0]:
                dq.clear()
            
            while dq and num > dq[-1][0]:
                dq.pop()
                
            dq.append((num, idx))
        
 
        result = []
        start = 0
        end = k
        dq = deque()
        
        for i in range(k):
                    
            increaseDQ(nums[i], i)            
                
        result.append(dq[0][0])            
        
        while end < len(nums):
                
            increaseDQ(nums[end], end) 
            if start == dq[0][1]:
                dq.popleft()   
            result.append(dq[0][0])              
            
            start += 1
            end += 1
            
        return result
            
