class Solution:
    def maxSum(self, n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(n + 1):
            dp[i] = max(i, dp[i // 2] + dp[i // 3] + dp[i // 4])
        return dp[n]

'''
    dp[i] = max(i, dp[i//2] + dp[i//3] + dp[i//4])
    either keep i as-is, or break into 3 parts recursively
    bottom-up ensures subproblems solved before needed
    time complexity : O(n)
    space complexity : O(n)
'''
