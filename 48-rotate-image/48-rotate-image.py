class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        for y, row in enumerate(matrix):
            if y >= n // 2:
                break
            for x, num in enumerate(row[y:-y-1], y):
                matrix[y][x] = matrix[n-1-x][y]
                matrix[n-1-x][y] = matrix[n-y-1][n-x-1] 
                matrix[n-y-1][n-x-1] = matrix[x][n-y-1]
                matrix[x][n-y-1] = num
               
            
                