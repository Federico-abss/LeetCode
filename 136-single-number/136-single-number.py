class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        acc = 0
        
        for num in nums:
            acc = acc ^ num
            
        return acc
        