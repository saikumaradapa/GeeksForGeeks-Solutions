class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:

        n = len(arr)
        INF = float('inf')

        # pre_min[i] / pre_max[i] = min / max of arr[0 .. i-1]   (empty when i = 0)
        pre_min = [INF] * (n + 1)
        pre_max = [-INF] * (n + 1)
        for i in range(n):
            pre_min[i + 1] = min(pre_min[i], arr[i])
            pre_max[i + 1] = max(pre_max[i], arr[i])

        # suf_min[i] / suf_max[i] = min / max of arr[i .. n-1]   (empty when i = n)
        suf_min = [INF] * (n + 1)
        suf_max = [-INF] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], arr[i])
            suf_max[i] = max(suf_max[i + 1], arr[i])

        best = INF
        # remove window [i, i+k-1]; remaining = arr[0..i-1] + arr[i+k..n-1]
        for i in range(n - k + 1):
            hi = max(pre_max[i], suf_max[i + k])
            lo = min(pre_min[i], suf_min[i + k])
            if hi - lo < best:
                best = hi - lo

        return best
