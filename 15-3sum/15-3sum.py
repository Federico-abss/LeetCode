class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for l, num in enumerate(nums[:-2]):
            if l > 0 and nums[l-1] == nums[l]:
                continue
            idx, r = l+1, len(nums)-1
            
            while idx < r:
                threeSum = num+nums[idx]+nums[r] 
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    idx += 1
                else:
                    result.append([num, nums[idx], nums[r]])
                    
                    while idx < r and nums[r] == nums[r-1]:
                        r-=1
                    while idx < r and nums[idx] == nums[idx+1]:
                        idx+=1
                    r-=1
                    idx+=1
                  
                    
        return result
                
                    
                    
        