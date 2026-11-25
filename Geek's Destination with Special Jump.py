class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        c = a - b

        def S(m):
            if m <= 0:
                return 0
            q, rem = divmod(m, c)
            return c * q * (q + 1) // 2 + rem * (q + 1)

        def G(n):
            return S(n - a)

        x1, x2 = d - r, d - l
        cnt = x2 - x1 + 1
        total_x = (x1 + x2) * cnt // 2
        total = total_x + 2 * b * (G(x2) - G(x1 - 1)) + cnt
        return total % MOD
