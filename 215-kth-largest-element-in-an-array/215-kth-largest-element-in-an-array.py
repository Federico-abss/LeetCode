class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = len(nums)
        k = right - k
        
        while True:
            cur = right - 1
            pivot = nums[cur]
        
            for idx in range(left, right):
                if idx >= cur:
                    if cur == k:
                        return nums[cur]
                    elif cur < k:
                        left = cur
                    else:
                        right = cur
                    break
                        
                while nums[idx] > pivot:
                    if idx + 1 < cur:
                        nums[cur], nums[cur-1] = nums[cur-1], nums[cur]
                    nums[idx], nums[cur] = nums[cur], nums[idx]
                    cur -= 1
                    
                
                    
                
                    
                
        