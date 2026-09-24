class Solution:
    def maxStackHeight(self, r, h):

        n = len(r)
        MAXH = 1000                      # h[i] <= 1000

        # max-Fenwick (BIT) indexed by HEIGHT: tree[k] holds the best stack height
        # achievable ending with a disc whose height maps into that range
        tree = [0] * (MAXH + 1)

        def update(i, val):
            while i <= MAXH:
                if val > tree[i]:
                    tree[i] = val
                i += i & (-i)

        def query(i):                    # max over heights [1..i]
            res = 0
            while i > 0:
                if tree[i] > res:
                    res = tree[i]
                i -= i & (-i)
            return res

        # process discs in increasing RADIUS; index the BIT by HEIGHT
        # -> querying heights < h[i] gives the best chain among discs with
        #    (radius < r[i]) AND (height < h[i]), enforcing BOTH strict constraints
        order = sorted(range(n), key=lambda k: (r[k], h[k]))

        dp = [0] * n
        best = 0
        idx = 0
        while idx < n:
            # group all discs sharing the same radius; compute their dp using the
            # BIT state BEFORE inserting the group, so equal-radius discs can't stack
            j = idx
            cur_r = r[order[idx]]
            group = []
            while j < n and r[order[j]] == cur_r:
                group.append(order[j])
                j += 1

            for k in group:
                prev = query(h[k] - 1)   # best chain with strictly smaller r and h
                dp[k] = h[k] + prev
                if dp[k] > best:
                    best = dp[k]

            for k in group:              # now publish the group into the BIT
                update(h[k], dp[k])

            idx = j

        return best
