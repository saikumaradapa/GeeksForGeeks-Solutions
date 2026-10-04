from typing import List

class Solution:
    def findPerimeter(self, mat: List[List[int]]) -> int:
        perimeter = 0 
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += self.getUnitPerimeter(i, j, n, m, mat)
        return perimeter
    
    def getUnitPerimeter(self, i, j, n, m, mat):
        cnt = 0 
        if i == 0 or mat[i-1][j] == 0:
            cnt += 1
        if j == 0 or mat[i][j-1] == 0:
            cnt += 1
        if i == n - 1 or mat[i+1][j] == 0:
            cnt += 1
        if j == m - 1 or mat[i][j+1] == 0:
            cnt += 1
        
        return cnt 
