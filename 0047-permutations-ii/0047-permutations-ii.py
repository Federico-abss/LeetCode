class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        def unique_perms(nums, cur):
            if not nums:
                result.add(tuple(cur))
                
            for idx, num in enumerate(nums):
                unique_perms(nums[:idx] + nums[idx+1:], cur + [num])
                
        unique_perms(nums, [])
        return result