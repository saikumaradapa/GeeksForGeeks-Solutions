class Solution:
    def findWays(self, n):
        if n % 2 == 1:
            return 0
        
        k = n // 2  # number of bracket pairs
        
        # Compute nCr(2k, k)
        res = 1
        for i in range(k):
            res = res * (2 * k - i) // (i + 1)
        
        # Catalan number
        return res // (k + 1)
