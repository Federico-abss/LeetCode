class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        stack = []
        result = 0
        seen = {}
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                
                if val:
                    stack.append((val,r,c,0))
        
        moves = [[0,-1],[-1,0],[0,1],[1,0]]
        
        def neighbor(r,c):
                        
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                return grid[r][c]
            else:
                return 0
            
        while stack:
            
            val, r, c, mvs = stack.pop()
            while len(seen) > mvs:
                seen.popitem()
            
            seen[(r,c)] = "#"
            result = max(result, val)
            
            for move in moves:
                R = r + move[0]
                C = c + move[1]
                if (R, C) in seen:
                    continue
                    
                addVal = neighbor(R, C)
                if addVal:
                    stack.append((val + addVal, R, C, mvs + 1))
                    
        return result
