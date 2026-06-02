class Solution:
    def sumDiffPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        res = 0
        i = n - 1
        while i > 0:
            if arr[i] - arr[i - 1] < k:
                res += arr[i] + arr[i - 1]
                i -= 2          # both used, disjoint
            else:
                i -= 1          # drop largest, it can't pair
        return res

'''
    sort ascending, greedily pair from the largest end
    adjacent elements have the smallest difference, so only check neighbors
    if arr[i] - arr[i-1] < k, pair them and skip both (disjoint)
    else drop arr[i] (can't pair with anything smaller)
    time complexity : O(n log n)
    space complexity : O(1) (or O(n) for sort)
'''
