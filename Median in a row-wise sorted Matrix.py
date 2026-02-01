class Solution:
    def median(self, mat):
        n, m = len(mat), len(mat[0])
        low = min(row[0] for row in mat)
        high = max(row[m-1] for row in mat)
        target = (n * m) // 2

        while low <= high:
            mid = (low + high) // 2
            count = 0
            
            # one line to find upper bound
            # count = sum(bisect.bisect_right(row, mid) for row in mat)

            for row in mat:
                count += self.upper_bound(row, mid)

            if count <= target:
                low = mid + 1
            else:
                high = mid - 1

        return low

    # Returns count of elements ≤ x in sorted row
    def upper_bound(self, row, x):
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        return l


''' Binary search on values | optimal 
    time complexity : O(n log m log V)
    space complexity : O(1)
'''
