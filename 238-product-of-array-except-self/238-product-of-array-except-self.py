class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        @cache
        def calculateProductLeft(idx):
            if idx < 0:
                return 1
            
            return nums[idx] * calculateProductLeft(idx - 1)
        
        @cache
        def calculateProductRight(idx):
            if idx == len(nums):
                return 1
            
            return nums[idx] * calculateProductRight(idx + 1)
        
        result = [0] * len(nums)
        
        for idx in range(len(nums)):
            result[idx] = calculateProductLeft(idx-1) * calculateProductRight(idx+1)
            
        return result
            