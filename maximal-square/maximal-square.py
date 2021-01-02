class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        neighbors = [[0, 1], [1,1], [1,0]]
        maxSquare = 0
        
        def adj(x, y):
            nonlocal maxSquare
            
            if dp[y][x] != None:
                return dp[y][x]
            
            square = 301
            
            for neighbor in neighbors:                
                X, Y = x + neighbor[0], y + neighbor[1]
                
                if X < len(matrix[0]) and Y < len(matrix):                    
                    square = min(adj(X, Y), square)
                    
                else:
                    square = 0
                    
            res = dp[y][x] = square + 1 if matrix[y][x] == "1" else 0
            maxSquare = max(maxSquare, res)
            return res
        
        adj(0,0)
        return maxSquare ** 2
              
            
