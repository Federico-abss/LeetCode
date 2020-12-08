class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        result = []
        idx = 0
        
        if not nums:
            if lower != upper:
                return [str(lower) + "->" + str(upper)]
            else:
                return [str(upper)]
      
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        
        while idx < len(nums) - 1:
            
            if nums[idx] < nums[idx + 1] - 1:
                if nums[idx] == nums[idx + 1] - 2:
                    result.append(str(nums[idx] + 1))
                else:
                    result.append(str(nums[idx] + 1) + "->" + str(nums[idx + 1] - 1))
            
            idx += 1
                    
        return result
