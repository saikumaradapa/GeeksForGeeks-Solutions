class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)
        # no_skip = max subarray sum ending at i with no element skipped
        # one_skip = max subarray sum ending at i with one element skipped
        no_skip = arr[0]
        one_skip = float('-inf')
        res = arr[0]

        for i in range(1, n):
            # skip arr[i]: extend previous no_skip (now one element skipped)
            # don't skip: extend no_skip normally, or start fresh
            one_skip = max(one_skip + arr[i], no_skip)
            no_skip = max(no_skip + arr[i], arr[i])
            res = max(res, no_skip, one_skip)

        return res
