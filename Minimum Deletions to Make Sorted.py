from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        lis = []

        for x in arr:
            idx = bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x

        return len(arr) - len(lis)
