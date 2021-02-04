class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()
        result = 0
        hmap = defaultdict(int)
        
        for num in nums:
            hmap[num] += 1
            
        prev = nums[0] - 2
        
        for key,value in hmap.items():
            
            if key - 1 == prev:
                result = max(result, hmap[key] + hmap[prev])
                
            prev = key
            
        return result