class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = len(nums)
        k = right - k
        
        while True:
            minLeft = left - 1
            pivot = nums[right-1]
        
            for idx in range(left, right):
                if nums[idx] < pivot:
                    minLeft += 1
                    nums[idx], nums[minLeft] = nums[minLeft], nums[idx]
                    
            minLeft += 1
            nums[idx], nums[minLeft] = nums[minLeft], nums[idx]
            if minLeft == k:
                return nums[minLeft]
            elif minLeft < k:
                left = minLeft + 1
            else:
                right = minLeft
            
                    
                
                    