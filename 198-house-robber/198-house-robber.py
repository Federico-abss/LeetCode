class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0] + nums
        for idx in range(3, len(nums)):
            nums[idx] += max(nums[idx-2], nums[idx-3])
        
        return max(nums[-2:])