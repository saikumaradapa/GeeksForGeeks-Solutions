from functools import lru_cache

class Solution:
    def minCount(self, arr):
        n = len(arr)

        # last_inc / last_dec: index of last element placed in each subsequence,
        # -1 means empty. Use value 0 as sentinel (since arr[i] >= 1) to keep
        # the state comparable; we pass indices and read arr[idx], with -1 -> no constraint.

        @lru_cache(None)
        def dfs(i, last_inc, last_dec):
            if i == n:
                return 0

            # option 1: skip current element
            best = dfs(i + 1, last_inc, last_dec)

            # option 2: put arr[i] into the strictly INCREASING subsequence
            if last_inc == -1 or arr[i] > arr[last_inc]:
                best = max(best, 1 + dfs(i + 1, i, last_dec))

            # option 3: put arr[i] into the strictly DECREASING subsequence
            if last_dec == -1 or arr[i] < arr[last_dec]:
                best = max(best, 1 + dfs(i + 1, last_inc, i))

            return best

        max_included = dfs(0, -1, -1)
        return n - max_included


####################################
# tabulation 


class Solution:
    def minCount(self, arr):
        n = len(arr)
        # dp[i][last_inc][last_dec], i in 1..n+1, last_* in 0..n (0 = empty)
        # arr is read as arr[i-1] for 1-based index i
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for last_inc in range(n, -1, -1):
                for last_dec in range(n, -1, -1):
                    best = dp[i + 1][last_inc][last_dec]      # skip

                    # increasing: empty (0) or arr[i-1] > arr[last_inc-1]
                    if last_inc == 0 or arr[i-1] > arr[last_inc-1]:
                        best = max(best, 1 + dp[i + 1][i][last_dec])

                    # decreasing
                    if last_dec == 0 or arr[i-1] < arr[last_dec-1]:
                        best = max(best, 1 + dp[i + 1][last_inc][i])

                    dp[i][last_inc][last_dec] = best

        return n - dp[1][0][0]
