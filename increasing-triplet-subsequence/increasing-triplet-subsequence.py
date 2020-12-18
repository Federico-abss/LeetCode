class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = idx = 0
        second = None
        
        while idx < len(nums):
            
            if nums[idx] > nums[first]:
                if second and nums[idx] > nums[second]:
                    return True
                elif not second or (second and nums[idx] < nums[second]):
                    second = idx
            elif nums[idx] < nums[first]:
                first = idx
            
            idx += 1
        
        return False
