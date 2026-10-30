from typing import List

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:

        MOD = 10**9 + 7
        n = len(arr)

        # frequency of each value (arr[i] <= n, r <= n)
        size = max(n, r) + 2
        cnt = [0] * size
        for x in arr:
            cnt[x] += 1

        # pow2[k] = 2^k mod MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        total = 0
        P = 1        # product over v < m of (2^cnt[v] - 1): pick >= 1 copy of each
        used = 0     # number of elements with value < m

        for m in range(r + 1):
            # free elements = values not in 0..m (copies of m must all be excluded)
            free = n - used - cnt[m]
            if m >= l:
                total = (total + P * pow2[free]) % MOD

            # extend the prefix to include value m for the next MEX
            P = P * (pow2[cnt[m]] - 1) % MOD
            used += cnt[m]
            if P == 0:
                break            # value m is missing -> no larger MEX is possible

        return total
