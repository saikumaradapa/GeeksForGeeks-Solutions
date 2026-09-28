from math import gcd

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        # Segment tree stored in an array; size 2*n with leaves at [n, 2n)
        tree = [0] * (2 * n)

        # Build: place leaves, then fill internal nodes bottom-up
        for i in range(n):
            tree[n + i] = arr[i]
        for i in range(n - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])

        def update(index: int, value: int) -> None:
            i = index + n
            tree[i] = value
            i //= 2
            while i >= 1:
                tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
                i //= 2

        def query(l: int, r: int) -> int:
            # GCD over [l, r] inclusive
            res = 0  # gcd(0, x) == x, so 0 is a safe identity
            l += n
            r += n + 1  # make r exclusive
            while l < r:
                if l & 1:
                    res = gcd(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = gcd(res, tree[r])
                l //= 2
                r //= 2
            return res

        ans = []
        for q in queries:
            if q[0] == 0:          # Type 1: range GCD query
                ans.append(query(q[1], q[2]))
            else:                  # Type 2: point update
                update(q[1], q[2])
        return ans
