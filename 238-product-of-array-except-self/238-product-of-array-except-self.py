class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        right = 1
        
        for idx, num in enumerate(nums[::-1]):
            result[-idx-1] = right
            right *= num
        
        left = 1
        for idx, num in enumerate(nums):
            result[idx] *= left
            left *= num
            
        return result
            