class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = self.binarySearch(nums, target), self.binarySearch(nums, target+1)-1
        if nums and left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]
        
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)
        
        while start < end:
            mid = start + (end - start) // 2
            
            if (nums[mid] >= target):
                end = mid
            else:
                start = mid + 1
                
        return start
            