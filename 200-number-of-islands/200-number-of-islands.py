class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        
        def explore(x: int, y: int):
            if x >= n or y >= m or x < 0 or y < 0:
                return
            
            if grid[y][x] == "1":
                grid[y][x] = "0"
                explore(x, y+1)
                explore(x, y-1)
                explore(x+1, y)
                explore(x-1, y)
                
        
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    islands += 1
                    explore(x, y)
                
        return islands
        
                