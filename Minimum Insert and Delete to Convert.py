class Solution:
    def minInsAndDel(self, a, b):
        from bisect import bisect_left

        n, m = len(a), len(b)

        # map b values to their index for O(1) lookup
        pos = {}
        for i, val in enumerate(b):
            pos[val] = i

        # filter a: only keep elements present in b, replace with their index in b
        mapped = []
        for val in a:
            if val in pos:
                mapped.append(pos[val])

        # LIS on mapped = LCS of a and b (since b is sorted and distinct)
        tails = []
        for x in mapped:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        lcs = len(tails)
        return (n - lcs) + (m - lcs)
