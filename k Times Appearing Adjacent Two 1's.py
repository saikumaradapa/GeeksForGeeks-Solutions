class Solution:
    def countStrings(self, n, k):
        MOD = 10**9 + 7

        # dp[i][j][last] = ways to form string of length i with j adjacent 1-pairs
        # last = 0 (ends with 0) or 1 (ends with 1)
        # transition:
        #   append 0: dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
        #   append 1: dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j-1][1]
        #     (if last was 1, appending 1 creates new adjacent pair → j-1 → j)

        # dp[j][last]: space optimize on i
        dp = [[0, 0] for _ in range(k + 1)]
        # base: length 1
        dp[0][0] = 1  # "0", 0 adjacent pairs
        dp[0][1] = 1  # "1", 0 adjacent pairs

        for i in range(2, n + 1):
            ndp = [[0, 0] for _ in range(k + 1)]
            for j in range(k + 1):
                # append 0
                ndp[j][0] = (dp[j][0] + dp[j][1]) % MOD
                # append 1
                ndp[j][1] = dp[j][0] % MOD  # prev ended with 0, no new pair
                if j > 0:
                    ndp[j][1] = (ndp[j][1] + dp[j-1][1]) % MOD  # prev ended with 1, new pair
            dp = ndp

        return (dp[k][0] + dp[k][1]) % MOD
