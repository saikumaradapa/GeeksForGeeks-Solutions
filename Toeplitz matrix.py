class Solution:
    def isToeplitz(self, mat):
        ROWS, COLS = len(mat), len(mat[0])
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if mat[i][j] != mat[i-1][j-1]:
                    return False
        return True

''' 
    time complexity : O(n * m)
    space complexity : O(1)
'''
