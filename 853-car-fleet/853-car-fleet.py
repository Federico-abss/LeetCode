class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        q = []
        fleets = []
        for pos, sp in zip(position, speed):
            heappush(q, (-pos, sp))
            
        def catchesUp(ahead: int, spAhead: int, behind: int, spBehind: int) -> bool:
            if spAhead >= spBehind:
                return False
            catchup = (ahead - behind) * spAhead / (spBehind - spAhead)
            if ahead + catchup > target:
                return False
            return True
          
        revPos, sp = heappop(q)
        fleets = [(-revPos, sp)]    
        
        while q:
            revPos, sp = heappop(q)
            ahead, spAhead = fleets[-1]
            if not catchesUp(ahead, spAhead, -revPos, sp):
                fleets.append((-revPos, sp))
        
        return len(fleets)
                    
                
                    
                    
            