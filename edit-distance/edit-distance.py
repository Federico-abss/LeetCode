class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
   
        dpTable = [[0 for i in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        dpTable[0] = [i for i in range(len(word1) + 1)]
        
        def minNeighbor(r, c):
            
            return min(dpTable[r-1][c-1], dpTable[r][c-1]+1, dpTable[r-1][c]+1)
        
        
        for r in range(1, len(word2) + 1):
            dpTable[r][0] = r
            for c in range(1, len(word1) + 1):
                if word1[c-1] != word2[r-1]:
                    dpTable[r-1][c-1] += 1
                dpTable[r][c] = minNeighbor(r, c) 
        
        return dpTable[-1][-1]
