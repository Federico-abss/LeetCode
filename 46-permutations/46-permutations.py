class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def recursiveHelper(nums: List[int], result: List[int]):
            if not nums:
                results.append(result)
                return 
        
            for idx, num in enumerate(nums):
                recursiveHelper(nums[:idx]+nums[idx+1:], result + [num])
            
            
        recursiveHelper(nums, [])  
        return results
        
        