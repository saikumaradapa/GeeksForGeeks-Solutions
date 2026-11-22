class Solution:
    def longestSubarrayDivK(self, arr, k):
        first = {0: -1}
        total = 0
        best = 0
        for i, x in enumerate(arr):
            total = (total + x) % k
            if total in first:
                best = max(best, i - first[total])
            else:
                first[total] = i
        return best
