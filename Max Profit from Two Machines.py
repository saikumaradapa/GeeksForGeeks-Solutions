class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)
        diff = [(a[i] - b[i], i) for i in range(n)]
        diff.sort(reverse=True)

        lo = max(0, n - y)
        hi = min(x, n)

        # start with all to B, then greedily switch top ones to A
        base = sum(b)
        # gains[i] = a[idx] - b[idx] for sorted position i
        gains = [a[diff[i][1]] - b[diff[i][1]] for i in range(n)]

        # prefix sum of gains
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + gains[i]

        best = 0
        for k in range(lo, hi + 1):
            best = max(best, base + prefix[k])

        return best

'''
    sort by a[i]-b[i] descending
    start with all tasks on B (base sum)
    switching top k tasks to A adds sum of top k (a[i]-b[i]) values
    find optimal k in valid range [max(0,n-y), min(x,n)]
    time complexity : O(n log n)
    space complexity : O(n)
'''

#########################################################################################################

class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)

        # dp[i][j] = max profit for tasks 0..i-1 with j assigned to A
        # space optimized: only need previous row
        prev = [float('-inf')] * (x + 1)
        prev[0] = 0

        for i in range(n):
            curr = [float('-inf')] * (x + 1)
            for j in range(min(i + 1, x) + 1):
                if prev[j] == float('-inf'):
                    continue
                # assign task i to A
                if j + 1 <= x:
                    curr[j + 1] = max(curr[j + 1], prev[j] + a[i])
                # assign task i to B
                if (i - j) < y:
                    curr[j] = max(curr[j], prev[j] + b[i])
            prev = curr

        return max(prev)

'''
    dp[i][j] = max profit for first i tasks with j assigned to A
    assign to A: dp[i][j+1] = dp[i-1][j] + a[i]
    assign to B: dp[i][j] = dp[i-1][j] + b[i] (if B has capacity)
    space optimized to 1D
    time complexity : O(n * x)
    space complexity : O(x)
'''
