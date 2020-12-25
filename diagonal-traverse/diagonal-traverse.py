class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return
        
        x = y = 0
        N = len(matrix[0]) - 1
        M = len(matrix) - 1
        result = []
        
        
        def movement(x, y, mx, my):
            
            while 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
                
                result.append(matrix[y][x])
                
                x += mx
                y += my
                
            return x - mx, y - my
        
        mx = 1
        my = -1
        while True:
            
            x, y = movement(x, y, mx, my)
            if (x, y) == (N, M):
                break
                
            mx = -mx
            my = -my
            
            if not y and x < N  or y == M:
                x += 1
            else:
                y += 1
                
        return result
                
            
