class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        
        while l < r:
            mid = (l+r)//2
            if (nums[mid]<nums[r]):
                r = mid 
            else:
                l = mid + 1
            
        searchLeft = self.binSearch(nums[:l], target)
        searchRight = self.binSearch(nums[l:], target)
        if searchLeft >= 0:
            return searchLeft
        elif searchRight >= 0:
            return searchRight + l
        else:
            return -1
    
    
    def binSearch(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            recursiveResult = self.binSearch(nums[mid+1:], target) + 1
            return mid + recursiveResult if recursiveResult > 0 else -1
        else:
            return self.binSearch(nums[:mid], target)