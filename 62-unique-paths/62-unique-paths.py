def incrementPath(grid: List[List[int]], x: int, y: int):
    if x == len(grid[0]):
        return
    
    prevSteps = 0
    if x or y:
        if x:
            prevSteps = grid[y][x-1]
        if y:
            prevSteps += grid[y-1][x]
    else:
        prevSteps = 1
    grid[y][x] += prevSteps
    incrementPath(grid, x+1, y)
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for y in range(m):
            incrementPath(grid, 0, y)
        
        return grid[-1][-1]
    
    
    