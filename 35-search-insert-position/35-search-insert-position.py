class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)
        
        while l < r:
            mid = l + (r-l)//2
            
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
            
        return l