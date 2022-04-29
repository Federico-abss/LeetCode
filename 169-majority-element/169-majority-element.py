class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        appearences = 1
        candidate = None
        
        for num in nums:
            if num != candidate:
                appearences -= 1
            else:
                appearences += 1
                
            if appearences == 0:
                candidate = num
                appearences = 1
                
        return candidate
                