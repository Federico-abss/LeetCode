class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        if nums[0] < 0 and nums[-1] >= 0:
            
            pos = neg = 0
            while nums[pos] < 0:
                pos += 1
            neg = pos-1
            
            result = []
            while neg >= 0 and pos < len(nums):
                if abs(nums[neg]) > nums[pos]:
                    result.append(pow(nums[pos],2))
                    pos += 1
                else:
                    result.append(pow(nums[neg],2))
                    neg -= 1
                
            while neg >= 0: 
                result.append(pow(nums[neg],2))
                neg -= 1
            while pos < len(nums):
                result.append(pow(nums[pos],2))
                pos += 1
                
            return result
        
        elif nums[-1] < 0:
            return reversed(list(map(lambda x: pow(x,2),nums)))
        
        else:
            return list(map(lambda x: pow(x,2),nums))
