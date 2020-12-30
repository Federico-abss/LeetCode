class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        surroundings = [[-1,-1],[-1,0],[-1,1],
                        [0, -1],       [0, 1],
                        [1, -1],[1, 0],[1, 1]]
        
        def neighbors(x, y) -> int:
            
            neighbors = 0
            for sur in surroundings:
                X, Y = x + sur[1], y + sur[0]
                
                if 0 <= X < len(board[0]) and 0 <= Y < len(board):
                    
                    neighbors += int(board[Y][X] > 0)
            
            return neighbors
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                neighs = neighbors(c, r)
                if (neighs < 2 or neighs > 3) and board[r][c]:
                    board[r][c] += 1
                if neighs == 3 and not board[r][c]:
                    board[r][c] -= 1
                      
        for r in range(len(board)):
            for c in range(len(board[0])):
                        
                if board[r][c] > 1:
                    board[r][c] = 0
                elif board[r][c] < 0:
                    board[r][c] = 1
                        
