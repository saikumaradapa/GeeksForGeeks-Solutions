class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:

        lo = 0
        hi = min(s1, s2) * n        # the faster scanner alone always finishes by then

        while lo < hi:
            mid = (lo + hi) // 2
            # documents both scanners can finish within 'mid' time
            if mid // s1 + mid // s2 >= n:
                hi = mid             # enough -> try a smaller time
            else:
                lo = mid + 1         # not enough -> need more time

        return lo
