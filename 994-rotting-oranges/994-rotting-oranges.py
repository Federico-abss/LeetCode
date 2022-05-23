class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = ((-1,0), (0,-1), (1, 0), (0, 1))
        #flattenedGrid = [0] * m * n
        rotten = deque()
        global fresh
        fresh = 0
        
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                #position = y * m + x
                if cell == 2:
                    #flattenedGrid[position] = position
                    rotten.append((x, y))
                elif cell == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        def rot(x: int, y: int):
            global fresh
            
            for movx, movy in directions:
                X, Y = x + movx, y + movy
                if 0 <= X < n and 0 <= Y < m and grid[Y][X] == 1:
                    grid[Y][X] = 2
                    rotten.append((X, Y))
                    fresh -= 1
        
        turns = 0
        rotten.append("#")
        while len(rotten) > 1:
            cur = rotten.popleft()
            if cur == "#":
                rotten.append("#")
                turns += 1
            else:
                rot(cur[0], cur[1])
               
        return -1 if fresh else turns
            
        
        #def union(par, child):
        
            
        
            
            