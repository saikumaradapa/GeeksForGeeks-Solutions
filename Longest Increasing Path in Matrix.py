class Solution:
    def longIncPath(self, matrix, n, m):
        dp = [[1] * m for _ in range(n)]
        cells = sorted(((matrix[i][j], i, j) for i in range(n) for j in range(m)))
        ans = 1
        for val, i, j in cells:
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] < val:
                    if dp[ni][nj] + 1 > dp[i][j]:
                        dp[i][j] = dp[ni][nj] + 1
            if dp[i][j] > ans:
                ans = dp[i][j]
        return ans
