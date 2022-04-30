class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = 0
        for num in nums:
            bit = 1 << (num-1)
            if cache & bit:
                return num
            cache |= bit
            
        