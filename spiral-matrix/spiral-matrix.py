class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] #r,d,l,u
        n, m = len(matrix), len(matrix[0])
        edx, edy = m, n
        count = y = turn = 0
        x = -1
        result = []
        
        while count < n*m:
            
            x += dirs[turn%4][1]
            y += dirs[turn%4][0]
            
            if (turn % 4 == 0 and x >= edx) or (turn % 4 == 2 and x < edx) or \
               (turn % 4 == 1 and y >= edy) or (turn % 4 == 3 and y < edy):
                x -= dirs[turn%4][1]
                y -= dirs[turn%4][0]
                
                turn += 1
                
                if turn % 4 == 0:
                    edx = m - turn // 4
                elif turn % 4 == 1:
                    edy = n - turn // 4
                elif turn % 4 == 2:
                    edx = 0 + turn // 4
                elif turn % 4 == 3:
                    edy = 0 + (turn + 1)// 4
                
            else:
                result.append(matrix[y][x])            
                count += 1
            
        return result
