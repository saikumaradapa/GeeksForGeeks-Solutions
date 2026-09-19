class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:

        m, n = len(s1), len(s2)

        # dp[j] = min cost to make s1[:i] and s2[:j] identical (rolling row over i)
        # base: empty s1 vs s2[:j] -> delete all j chars of s2
        prev = [0] * (n + 1)
        for j in range(1, n + 1):
            prev[j] = prev[j - 1] + costS2

        for i in range(1, m + 1):
            cur = [0] * (n + 1)
            cur[0] = prev[0] + costS1          # s1[:i] vs empty -> delete all i chars of s1
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = prev[j - 1]        # chars match -> keep both, no cost
                else:
                    # delete from s1 (cost costS1) or delete from s2 (cost costS2)
                    cur[j] = min(prev[j] + costS1, cur[j - 1] + costS2)
            prev = cur

        return prev[n]


