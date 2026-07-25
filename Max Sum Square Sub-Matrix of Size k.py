class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)

        # Build prefix sum matrix
        # prefix[i][j] = sum of all elements in mat[0..i-1][0..j-1]
        prefix = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1]
                                + prefix[i-1][j]
                                + prefix[i][j-1]
                                - prefix[i-1][j-1])

        max_sum = float('-inf')

        # Iterate over all possible k×k sub-grids
        # Bottom-right corner at (i, j) in 1-indexed prefix matrix
        for i in range(k, n + 1):
            for j in range(k, n + 1):
                total = (prefix[i][j]
                         - prefix[i-k][j]
                         - prefix[i][j-k]
                         + prefix[i-k][j-k])
                max_sum = max(max_sum, total)

        return max_sum
