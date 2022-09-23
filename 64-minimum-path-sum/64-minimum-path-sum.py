class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache
        def minSearch(x, y):
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                return grid[y][x]
            
            elif x >= len(grid[0]) or y >= len(grid):
                return float("inf")
            
            return grid[y][x] + min(minSearch(x+1, y), minSearch(x, y+1))
                
        return minSearch(0,0)