class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        maxDist = nums[0]
        
        for idx, num in enumerate(nums[:-1]):
            if idx > maxDist:
                return False
            
            maxDist = max(maxDist, num + idx)

        
        return maxDist >= len(nums) - 1
        

        