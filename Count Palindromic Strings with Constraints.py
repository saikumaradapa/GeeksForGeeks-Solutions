class Solution:
    def palindromicStrings(self, n, k):

        MOD = 10**9 + 7

        # P[m] = number of ordered ways to pick m DISTINCT letters = k*(k-1)*...*(k-m+1)
        maxM = n // 2
        P = [1] * (maxM + 1)
        for m in range(1, maxM + 1):
            P[m] = P[m - 1] * (k - m + 1) % MOD

        total = 0
        for L in range(1, n + 1):
            if L % 2 == 0:
                # even length 2m: each half-letter appears exactly twice
                # => the m half-letters must all be distinct -> P(k, m)
                m = L // 2
                total = (total + P[m]) % MOD
            else:
                # odd length 2m+1: half has m distinct letters (each twice),
                # center is one letter NOT in the half (else it appears 3 times)
                m = (L - 1) // 2
                total = (total + P[m] * (k - m)) % MOD

        return total % MOD

''' time complexity : O(n)  (<= O(k^2) given n <= 2k)
    space complexity : O(n)
    approach to recall quickly

    - a palindrome is fully determined by its first half (+ a center if odd length)
    - mirroring makes every half-letter appear TWICE
    - constraint "no char more than twice" => all letters in the half must be DISTINCT
        -> ordered choice of m distinct letters = P(k, m) = k*(k-1)*...*(k-m+1)

    - EVEN length 2m : count = P(k, m)
    - ODD  length 2m+1: half = P(k, m), center must avoid the m used letters
                        (using a half-letter as center => 3 occurrences)
                        -> count = P(k, m) * (k - m)
    - length 1 is the odd case with m=0 -> P(k,0)*(k-0) = k

    - sum over all L from 1..n, all mod 1e9+7
    - verify: n=3,k=2 -> (L1:2)+(L2:2)+(L3:2)=6 ; n=4,k=3 -> 3+3+6+6=18
'''
