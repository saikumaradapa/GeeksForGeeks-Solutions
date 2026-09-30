class Solution:
    def ways(self, x: int, y: int) -> int:

        MOD = 10**9 + 7

        # need x left-moves and y down-moves in any order -> C(x + y, x)
        # DP grid: dp[i][j] = number of paths from (i, j) to origin
        dp = [[0] * (y + 1) for _ in range(x + 1)]

        for i in range(x + 1):
            for j in range(y + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 1        # only one straight path along an axis
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

        return dp[x][y]
