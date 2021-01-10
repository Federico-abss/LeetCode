class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
      
        hmap = defaultdict(int)
        patterns = []
        
        while True:
            
            temp = [0] * 8
            for j in range(1, 7):
                
                if cells[j - 1] == cells[j + 1]:
                    temp[j] = 1
            
            temp = tuple(temp)
            if temp not in hmap:
                patterns.append(temp)
            else:
                break            
            hmap[temp] += 1              
            cells = temp
            
        return patterns[(N - 1) % len(patterns)]   
            
