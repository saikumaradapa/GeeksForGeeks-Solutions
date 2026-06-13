class Solution:
    def computeValue(self, n):
        MOD = 10**9 + 7
        # answer = C(2n, n) mod MOD
        num = 1
        den = 1
        for i in range(n):
            num = num * (2 * n - i) % MOD
            den = den * (i + 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD
