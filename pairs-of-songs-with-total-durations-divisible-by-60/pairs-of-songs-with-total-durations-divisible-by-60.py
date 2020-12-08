class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        hmap = defaultdict(list)
        result = 0
        
        for i, t in enumerate(time):
            
            hmap[t%60].append(i)
        
        for t in time:
            
            key = (60 - t % 60) % 60
            if key in hmap:
                result += len(hmap[key])
                
                if key == 30 or not key:
                    result -= 1
                    
        return result//2
