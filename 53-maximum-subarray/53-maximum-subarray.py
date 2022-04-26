class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        start = end = lastNeg = 0
        windowSum = 0
        maxSum = -10000
        
        while end < len(nums):
            windowSum = nums[start]
            end += 1
            maxSum = max(maxSum, windowSum)
            while windowSum >= 0 and end < len(nums):
                if nums[end] < 0:
                    lastNeg = end
                    
                windowSum += nums[end]
                if windowSum < 0: 
                    start = lastNeg 
                    end = start + 1
                    break
                
                maxSum = max(maxSum, windowSum)
                end += 1
                
            start += 1
            
        return maxSum
                
                