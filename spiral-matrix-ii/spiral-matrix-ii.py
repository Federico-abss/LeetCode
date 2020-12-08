class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] #r,d,l,u
        y = turn = 0
        x = -1
        count = 1
        
        while count <= n*n:
            
            x += dirs[turn][1]
            y += dirs[turn][0]
                        
            if 0 > x or x >= n or 0 > y or y >= n or matrix[y][x]:
                    
                x -= dirs[turn][1]
                y -= dirs[turn][0]
                turn += 1
                
                if turn > 3:
                    turn %= 4
                x += dirs[turn][1]
                y += dirs[turn][0]
                    
            matrix[y][x] = count
            count += 1
                  
        return matrix
