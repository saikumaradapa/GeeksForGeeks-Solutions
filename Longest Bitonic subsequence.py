class Solution:
    def longestBitonicSequence(self, n, nums):
        dp1 = [1] * n  # LIS
        dp2 = [1] * n  # LDS

        # LIS from left
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[j])

        # LDS from right
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    dp2[i] = max(dp2[i], 1 + dp2[j])

        res = 0

        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:   # valid bitonic peak
                res = max(res, dp1[i] + dp2[i] - 1)

        return res
        
''' using longest increasing subsequence
    time complexity : O(n ^ 2)
    space complexity : O(n)
'''
