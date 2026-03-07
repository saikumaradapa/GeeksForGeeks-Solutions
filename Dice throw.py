
class Solution:
    def noOfWays(self, m, n, x):
        # Initialize the DP table
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case

        # Fill the DP table
        for i in range(1, n + 1):  # for each dice
            for j in range(1, x + 1):  # for each sum
                for face in range(1, m + 1):  # for each face value
                    if j - face >= 0:
                        dp[i][j] += dp[i - 1][j - face]

        return dp[n][x]
