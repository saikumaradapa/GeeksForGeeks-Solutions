class Solution:
    def findMax(self, n, a, b, k):
        # Difference array technique
        diff = [0] * (n + 1)

        for i in range(len(a)):
            diff[a[i]] += k[i]
            if b[i] + 1 <= n:
                diff[b[i] + 1] -= k[i]

        # Prefix sum to get actual values, track max
        max_val = 0
        curr = 0
        for i in range(n):
            curr += diff[i]
            if curr > max_val:
                max_val = curr

        return max_val
