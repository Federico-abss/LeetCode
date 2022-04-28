class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        idx = len(nums) - 2
        target = idx + 1
        
        while idx >= 0:
            if idx + nums[idx] >= target:
                target = idx
                
            if target == 0:
                return True
            
            idx -= 1
        
        
        return False
        

        