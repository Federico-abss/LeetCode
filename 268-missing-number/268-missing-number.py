class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        presentNumbers = 0
        for idx, n in enumerate(nums):
            presentNumbers ^= idx
            presentNumbers ^= n
            
        return presentNumbers ^ len(nums)