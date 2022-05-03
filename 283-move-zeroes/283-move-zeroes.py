class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nonZeroIdx = 0
        for idx, num in enumerate(nums):
            if num:
                nums[nonZeroIdx] = num
                nonZeroIdx += 1
        
        nums[nonZeroIdx:] = [0] * (len(nums) - nonZeroIdx)