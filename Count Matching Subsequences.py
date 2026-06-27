class Solution:
    def countWays(self, s1, s2):
        MOD = 10**9 + 7
        n, m = len(s1), len(s2)

        # dp[i][j] = number of subsequences of s1[0..i-1] equal to s2[0..j-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # empty s2 is a subsequence of any prefix of s1
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i-1][j]  # skip s1[i-1]
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

        
        return dp[n][m]
