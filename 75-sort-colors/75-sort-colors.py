class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        idx = 0
        zeroes = 0
        for i, num in enumerate(nums):
            if num == 0 and idx == i:
                idx += 1
                zeroes += 1
            elif num == 0:
                zeroes += 1
                nums[idx], nums[i] = nums[i], nums[idx]
                while nums[idx] == 0:
                    idx += 1
                
        idx = zeroes
        for i, num in enumerate(nums[zeroes:], zeroes):
            if num == 1 and idx == i:
                idx += 1
            elif num == 1:
                nums[idx], nums[i] = nums[i], nums[idx]
                while nums[idx] == 1:
                    idx += 1
                
        
        