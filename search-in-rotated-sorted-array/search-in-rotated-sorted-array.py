class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = dist = len(nums) // 2
        if nums[0] > target:
            
            low = high
            high = len(nums) - 1
            
            while low < high and low >= 0 and (nums[low] > nums[high] or nums[low] > target):
                
                if nums[low] > nums[high]:
                    low += 1 + ((high - low) // 2)
                else:
                    high -= 1 + ((high - low) // 2)
                    low -= 1 + ((high - low) // 2)
                    
                
        elif nums[0] < target:
            
            dist //= 2    
            while low < high and high < len(nums) and (nums[low] > nums[high] or nums[high] < target):
                
                if nums[low] > nums[high]:
                    high -= 1 + ((high - low) // 2)
                else:
                    low += 1 + ((high - low) // 2)
                    high += 1 + ((high - low) // 2)
                    
        
        else:
            return 0
                
        
        idx = bisect_left(nums[low:high+1], target) + low
        return idx if idx < len(nums) and (nums[idx] == target) else -1
