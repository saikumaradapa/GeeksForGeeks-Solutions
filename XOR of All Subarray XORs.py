class Solution:
    def subarrayXor(self, arr):

        n = len(arr)
        res = 0
        for i in range(n):
            # arr[i] appears in (i+1)*(n-i) subarrays; it survives only if that count is odd
            if ((i + 1) * (n - i)) & 1:
                res ^= arr[i]
        return res
