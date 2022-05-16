class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0: return 0
        
        row = len(grid) 
        col = len(grid[0])
        
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [-1 for _ in range(row*col)]
        
        def find(x):
            if parent[x]!= -1:
                return find(parent[x])
            return x
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[yroot] = xroot
            self.count -= 1
        
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count
                