class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        for idx, cell in enumerate(grid[0][1:], 1):
            grid[0][idx] += grid[0][idx-1]
        
        for y, row in enumerate(grid[1:], 1):
            for x, cell in enumerate(row):
                if x > 0:
                    grid[y][x] += min(grid[y][x-1], grid[y-1][x])
                else:
                    grid[y][x] += grid[y-1][x]
     
        return grid[-1][-1]