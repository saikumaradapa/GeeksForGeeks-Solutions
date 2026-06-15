class Solution:
    def minimumCost(self, cost, w):
        dp = [float('inf')] * (w + 1)
        dp[0] = 0

        for i in range(1, w + 1):
            for j in range(len(cost)):
                weight = j + 1
                if weight <= i and cost[j] != -1:
                    if dp[i - weight] != float('inf'):
                        dp[i] = min(dp[i], dp[i - weight] + cost[j])

        return dp[w] if dp[w] != float('inf') else -1
