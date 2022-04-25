class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        finalPosition = 0
        curPosition = 0
        
        while curPosition < len(nums):
            nums[finalPosition] = nums[curPosition]
            
            while curPosition < len(nums) and nums[curPosition] == nums[finalPosition]:
                curPosition += 1
            
            finalPosition += 1
            
        return finalPosition
            