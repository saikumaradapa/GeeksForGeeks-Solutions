class Solution:
    def compress(self, s):

        n = len(s)
        if n <= 1:
            return s

        # ---- Z-function of s ----
        # Z[i] = length of the longest substring starting at i that matches a prefix of s
        Z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i < r:
                Z[i] = min(r - i, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] > r:
                l, r = i, i + Z[i]

        # ---- best[L] = min tokens needed to grow prefix length L up to n ----
        INF = float('inf')
        best = [INF] * (n + 1)
        best[n] = 0
        for L in range(n - 1, 0, -1):
            best[L] = best[L + 1] + 1                       # append one literal char
            if 2 * L <= n and Z[L] >= L:                    # doubling is valid here
                best[L] = min(best[L], best[2 * L] + 1)     # '*' doubles current prefix

        # ---- reconstruct forward, preferring '*' whenever it stays optimal ----
        res = [s[0]]        # first token is always the literal s[0]
        L = 1
        while L < n:
            if 2 * L <= n and Z[L] >= L and best[2 * L] + 1 == best[L]:
                res.append('*')      # '*' (ascii 42) < any letter => lexicographically smaller
                L *= 2
            else:
                res.append(s[L])     # append literal, grow by 1
                L += 1

        return ''.join(res)

''' time complexity : O(n)
    space complexity : O(n)
    approach to recall quickly

    - decode rule: a '*' DOUBLES the current decoded string (appends it to itself)
    - so building s uses two moves on the prefix length L:
        * literal char : L -> L+1   (token = s[L])
        * star '*'      : L -> 2L    (valid only if s[0:L] == s[L:2L] and 2L <= n)
    - goal = MINIMUM number of tokens (primary), then lexicographically smallest (secondary)

    - check "s[0:L] == s[L:2L]" in O(1) using Z-array: valid iff Z[L] >= L
    - best[L] (backward DP): min tokens to go from prefix length L to n
        best[L] = min( best[L+1]+1 ,  best[2L]+1 if doubling valid )
    - reconstruct forward: at each L, if doubling is valid AND lies on an optimal
      path (best[2L]+1 == best[L]), take '*' — since '*' < any letter it is always
      the lexicographically smaller token, and it keeps the length minimal

    - WHY greedy-double-always fails: doubling too early can overshoot / strand you
      (e.g. "zzzzzzz" -> greedy gives "z**zzz" len6, optimal is "z*z*z" len5).
      The DP decides exactly when doubling actually shortens the result.
'''
