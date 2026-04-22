class Solution:
    def findMean(self, arr, queries):
        n = len(arr)

        # build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        res = []

        for l, r in queries:
            total = prefix[r + 1] - prefix[l]
            length = r - l + 1
            res.append(total // length)

        return res

''' use prefix sum to compute range sum in O(1) per query
    time complexity : O(n + q)
    space complexity : O(n)
'''
