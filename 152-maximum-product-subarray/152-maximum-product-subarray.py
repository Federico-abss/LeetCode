def maxProductSubs(nums: List[int]) -> int:
    if not nums: return 0

    product = 1
    maxProduct = nums[0]
    
    for num in nums[:]:
        product *= num
        maxProduct = max(maxProduct, product)
        
    if product > 0: return maxProduct
        
    product = 1
    for num in nums[::-1]:
        product *= num
        maxProduct = max(maxProduct, product)  
        
    return maxProduct
        
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = -float('inf')
        left = 0
        if 0 not in nums:
            return maxProductSubs(nums)
        
        for idx, num in enumerate(nums):
            if not num:
                result = max(maxProductSubs(nums[left:idx]), result)
                left = idx + 1
        else:
            result = max(maxProductSubs(nums[left:]), result)
        
            
        return max(result, 0)
        
        