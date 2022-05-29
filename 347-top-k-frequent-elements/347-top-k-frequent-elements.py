class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = defaultdict(int)
        
        for num in nums:
            hmap[num] += 1
            
        buckets = [0] * (len(nums)+1)
        result = []  
        for key, value in hmap.items():
            if not buckets[value]:
                buckets[value] = []
            buckets[value].append(key)
            
        for values in buckets[::-1]:
            if values:
                result += values
            if len(result) == k:
                break
            
        return result