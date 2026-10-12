class Solution:
    def minSquares(self, n, m):

        count = 0
        # repeatedly slice the largest possible squares off the longer side
        # (each cut goes fully across the remaining strip -> Euclidean algorithm)
        while n > 0 and m > 0:
            if n > m:
                n, m = m, n            # keep n <= m
            count += m // n            # cut off (m // n) squares of side n
            m %= n                     # leftover strip continues the process
        return count
