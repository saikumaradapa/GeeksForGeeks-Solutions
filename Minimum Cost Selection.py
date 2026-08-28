class Solution:
    def minCost(self, mat):

        # dp cost of ending at each of the 3 choices in the current row
        prev0, prev1, prev2 = mat[0][0], mat[0][1], mat[0][2]

        for i in range(1, len(mat)):
            cur0 = mat[i][0] + min(prev1, prev2)
            cur1 = mat[i][1] + min(prev0, prev2)
            cur2 = mat[i][2] + min(prev0, prev1)
            prev0, prev1, prev2 = cur0, cur1, cur2

        return min(prev0, prev1, prev2)

''' time complexity : O(n)
    space complexity : O(1)
    approach to recall quickly

    - classic "paint house" DP: pick one of 3 choices per row, no two adjacent
      rows share the same choice
    - dp[i][j] = min cost to reach row i choosing option j
              = mat[i][j] + min(dp[i-1][other two options])
    - keep only the previous row's 3 values (rolling variables) -> O(1) space
    - answer = min of the last row's three dp values
'''
