class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        start = 1
        windowSum = maxSum = nums[0]
        
        while start < len(nums):
        
            if windowSum < 0:
                windowSum = nums[start]
            else:
                windowSum += nums[start]
            maxSum = max(maxSum, windowSum)
                
            start += 1
            
        return maxSum
                
                