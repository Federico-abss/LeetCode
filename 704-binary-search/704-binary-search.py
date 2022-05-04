class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            recursiveResult = self.search(nums[mid+1:], target) + 1
            return mid + recursiveResult if recursiveResult > 0 else -1
        else:
            return self.search(nums[:mid], target)