def zeroMatrixRow(matrix: List[List[int]], x: int, y: int) -> None:
    matrix[y][x] = 0
    
    for idx, num in enumerate(matrix[y]):
        if num != None:
            matrix[y][idx] = 0
        else:
            zeroMatrixCol(matrix, idx, y)
            

def zeroMatrixCol(matrix: List[List[int]], x: int, y: int) -> None:
    matrix[y][x] = 0
            
    for i in range(len(matrix)):
        if matrix[i][x] != None:
            matrix[i][x] = 0
        else:
            zeroMatrixRow(matrix, x, i)
        
    

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for idx, row in enumerate(matrix):
            for col, num in enumerate(row):
                if not num:
                    matrix[idx][col] = None
                    
        for idx, row in enumerate(matrix):
            for col, num in enumerate(row):
                if num == None:
                    zeroMatrixRow(matrix, col, idx)
                    zeroMatrixCol(matrix, col, idx)
                    
                