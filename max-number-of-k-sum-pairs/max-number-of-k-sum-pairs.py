class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)
        result = 0
        
        for num in nums:
            if k - num in hmap:
                hmap[k - num] -= 1
                result += 1
                if not hmap[k - num]:
                    hmap.pop(k - num)
            else:                
                hmap[num] += 1
                    
        return result
