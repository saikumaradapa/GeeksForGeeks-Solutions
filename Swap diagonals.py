class Solution:
    def swapDiagonal(self, mat):
        n = len(mat)
        
        row, col = 0, n - 1
        for idx in range(n):
            mat[idx][idx], mat[row][col] = mat[row][col], mat[idx][idx]
            row += 1
            col -= 1
        
        return mat
    
