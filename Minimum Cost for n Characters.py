class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:

        # We need to consider lengths > n because we might overshoot with copy
        # then delete back to n. Max useful length is 2*n (copy from n doubles to 2n,
        # then delete n times). But practically we cap at 2*n.
        limit = 2 * n + 1
        INF = float('inf')
        dp = [INF] * limit
        dp[0] = 0

        for k in range(1, limit):
            # insert: from k-1 add one char
            if k - 1 >= 0 and dp[k - 1] < INF:
                dp[k] = min(dp[k], dp[k - 1] + i)

            # delete: from k+1 remove one char (handled when we set dp[k+1] and come back)
            # actually: dp[k] can come from dp[k+1] + d, but k+1 not computed yet
            # so handle delete as: from k, we can reach k-1 for cost d
            # but that's forward. Instead: dp[k] = min(dp[k], dp[k+1] + d) needs future.

            # copy: from k//2 if k is even
            if k % 2 == 0 and dp[k // 2] < INF:
                dp[k] = min(dp[k], dp[k // 2] + c)

        # Now handle deletions: dp[k] can improve dp[k-1] via delete
        # Since delete removes last char: from length k we reach k-1 at cost d
        # Process backward to propagate delete chains
        for k in range(limit - 1, 0, -1):
            if dp[k] < INF:
                dp[k - 1] = min(dp[k - 1], dp[k] + d)

        # But deletions and copies/inserts can interleave, so iterate until stable
        # Actually we need multiple passes since: insert/copy -> delete -> copy again
        # Use a proper BFS/relaxation approach instead

        # Reset and use proper forward DP with delete handled correctly
        dp = [INF] * limit
        dp[0] = 0

        for k in range(0, limit):
            if dp[k] == INF:
                continue

            # insert: k -> k+1
            if k + 1 < limit:
                dp[k + 1] = min(dp[k + 1], dp[k] + i)

            # copy: k -> 2k
            if 2 * k < limit:
                dp[2 * k] = min(dp[2 * k], dp[k] + c)

            # delete: k -> k-1 (propagate backwards after this pass)
            # handled in a backward sweep below

        # backward sweep for deletions (can chain multiple deletes)
        for k in range(limit - 1, 0, -1):
            dp[k - 1] = min(dp[k - 1], dp[k] + d)

        # But after deleting we might want to copy again, so we need to repeat
        # until convergence. Since copy doubles, O(log n) rounds suffice.
        changed = True
        while changed:
            changed = False
            for k in range(0, limit):
                if dp[k] == INF:
                    continue
                if k + 1 < limit and dp[k] + i < dp[k + 1]:
                    dp[k + 1] = dp[k] + i
                    changed = True
                if 2 * k < limit and dp[k] + c < dp[2 * k]:
                    dp[2 * k] = dp[k] + c
                    changed = True
            for k in range(limit - 1, 0, -1):
                if dp[k] + d < dp[k - 1]:
                    dp[k - 1] = dp[k] + d
                    changed = True

        return dp[n]

''' time complexity : O(n log n) amortized (O(log n) relaxation rounds over O(n) states)
    space complexity : O(n)
    approach to recall quickly

    - three operations on current length k:
        insert:  k -> k+1  cost i
        delete:  k -> k-1  cost d
        copy:    k -> 2k   cost c
    - dp[k] = min cost to reach exactly k characters
    - forward pass handles insert and copy (both increase or maintain length)
    - backward pass handles delete (decreases length)
    - operations can interleave (delete then copy, etc.) so repeat
      forward+backward passes until no improvement (converges in O(log n) rounds
      since copy doubles and is the only "long jump")
    - limit = 2n+1: we might overshoot to ~2n then delete back
'''
