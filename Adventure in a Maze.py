class Solution:
    def findWays(self, grid):

        MOD = 10**9 + 7
        n = len(grid)

        # dp_count[i][j] = number of valid paths from (i,j) to (n-1,n-1)
        # dp_max[i][j] = maximum adventure from (i,j) to (n-1,n-1), -1 if unreachable
        dp_count = [[0] * n for _ in range(n)]
        dp_max = [[-1] * n for _ in range(n)]

        # Base case: destination
        dp_count[n-1][n-1] = 1
        dp_max[n-1][n-1] = grid[n-1][n-1]

        # Fill bottom-up, right-to-left
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == n-1 and j == n-1:
                    continue

                val = grid[i][j]

                # Right move (val == 1 or val == 3)
                if (val == 1 or val == 3) and j + 1 < n:
                    if dp_count[i][j+1] > 0:
                        dp_count[i][j] = (dp_count[i][j] + dp_count[i][j+1]) % MOD
                        dp_max[i][j] = max(dp_max[i][j], val + dp_max[i][j+1])

                # Down move (val == 2 or val == 3)
                if (val == 2 or val == 3) and i + 1 < n:
                    if dp_count[i+1][j] > 0:
                        dp_count[i][j] = (dp_count[i][j] + dp_count[i+1][j]) % MOD
                        dp_max[i][j] = max(dp_max[i][j], val + dp_max[i+1][j])

        # If no valid path exists, return [0, 0] not [0, -1]
        if dp_count[0][0] == 0:
            return [0, 0]

        return [dp_count[0][0], dp_max[0][0]]

''' time complexity : O(n^2)
    space complexity : O(n^2)
    approach to recall quickly

    - dp from bottom-right to top-left
    - each cell can go right (val 1 or 3) or down (val 2 or 3)
    - dp_count[i][j] = sum of counts from reachable neighbors
    - dp_max[i][j] = grid[i][j] + max of dp_max from reachable neighbors
    - only consider neighbors that have valid paths (count > 0)
    - base case: dp_count[n-1][n-1] = 1, dp_max[n-1][n-1] = grid[n-1][n-1]
    - if no path exists (count == 0), return [0, 0]
'''
