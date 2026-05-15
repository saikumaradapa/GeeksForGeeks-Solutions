class Solution:
    def optimalKeys(self, n: int) -> int:
        # dp[i] = max A's with i key presses
        dp = list(range(n + 1))  # base: just press A i times

        for i in range(1, n + 1):
            # try: at some point j, do Ctrl+A, Ctrl+C, then paste (i-j-2) times
            # that multiplies dp[j] by (i - j - 1)
            for j in range(i - 3, 0, -1):
                # j presses to build, 1 for Ctrl+A, 1 for Ctrl+C, (i-j-2) pastes
                # total on screen = dp[j] * (i - j - 1)
                dp[i] = max(dp[i], dp[j] * (i - j - 1))

        return dp[n]

'''
    dp[i] = max A's achievable with exactly i presses
    for each i, either just type A (dp[i] = dp[i-1] + 1 from initialization)
    or at some earlier point j, select+copy then paste (i-j-2) times
    multiplies dp[j] by (i-j-1) since original + (i-j-2) pastes = (i-j-1) copies
    time complexity : O(n^2)
    space complexity : O(n)
'''
