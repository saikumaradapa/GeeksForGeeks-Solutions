class Solution:
    def totalWays(self, arr, target):
        total = sum(arr)
        
        # Edge cases
        if abs(target) > total:
            return 0
        
        if (target + total) % 2 != 0:
            return 0
        
        subset_sum = (target + total) // 2
        
        # DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to make sum 0
        
        for num in arr:
            # Traverse backwards to avoid reuse
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]
