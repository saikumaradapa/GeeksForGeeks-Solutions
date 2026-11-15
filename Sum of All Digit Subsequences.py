class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        total = sum(int(c) for c in s)
        return total * pow(2, len(s) - 1, MOD) % MOD
