class Solution:
    def diagView(self, mat):
        n = len(mat)
        res = []

        # Start from first row
        for c in range(n):
            i = 0
            j = c
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1

        # Start from last column (excluding first row)
        for r in range(1, n):
            i = r
            j = n - 1
            while i < n and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1

        return res

''' 
    time complexity : O(n^2)
    space complexity : O(1)
'''

#######################################################################################################################


class Solution:
    def diagView(self, mat):
        n = len(mat)
        res = []

        for s in range(2*n - 1):   # diagonal sum
            for i in range(n):
                j = s - i
                if 0 <= j < n:
                    res.append(mat[i][j])
        return res

''' 
    in diagonal matrix, for all anti-diagonal elements i + j = constant
    time complexity : O(n^2)
    space complexity : O(1)
'''
