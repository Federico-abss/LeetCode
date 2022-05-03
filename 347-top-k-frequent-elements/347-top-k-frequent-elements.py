class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = defaultdict(int)
        
        for num in nums:
            hmap[num] += 1
            
        q = []
        result = []
        for key, value in hmap.items():
            heappush(q , (-value, key))
            
        for _ in range(k):
            result.append(heappop(q)[1])
            
        return result