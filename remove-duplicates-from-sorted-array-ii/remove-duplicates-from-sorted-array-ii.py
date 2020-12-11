class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur = [-1,1]
        noEmpty = 0
        
        for i in range(len(nums)):
            
            if nums[i] == cur[0] and cur[1] == 2:
                nums[i] = -1
                noEmpty += 1
                
            elif nums[i] == cur[0]:
                cur[1] += 1
                nums[i-noEmpty] = cur[0] 
            
            else:
                cur = [nums[i], 1]
                nums[i-noEmpty] = cur[0] 
                
        return len(nums) - noEmpty
                
            
            
            
