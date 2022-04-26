class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()
        
        if nums[-1] >= 0 and prod(nums[0:2]) > prod(nums[-3:-1]):
            return prod(nums[0:2]) * nums[-1]
        else:
            return prod(nums[-3:])

                    
                    