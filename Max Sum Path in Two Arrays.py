class Solution:
    def maxPathSum(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        sum_a, sum_b = 0, 0
        result = 0

        while i < n and j < m:
            if a[i] < b[j]:
                sum_a += a[i]
                i += 1
            elif b[j] < a[i]:
                sum_b += b[j]
                j += 1
            else:
                # common element: take max path so far + common element
                result += max(sum_a, sum_b) + a[i]
                sum_a = 0
                sum_b = 0
                i += 1
                j += 1

        # remaining elements
        while i < n:
            sum_a += a[i]
            i += 1
        while j < m:
            sum_b += b[j]
            j += 1

        result += max(sum_a, sum_b)
        return result
