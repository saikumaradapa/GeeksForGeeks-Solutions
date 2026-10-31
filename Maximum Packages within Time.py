class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:

        n = len(arr)
        w = min(totalTime, n)          # window size: can't visit more than n locations

        cur = sum(arr[:w])             # first window: locations 0 .. w-1
        best = cur

        for i in range(w, n):
            cur += arr[i] - arr[i - w] # slide: add the new location, drop the oldest
            if cur > best:
                best = cur

        return best
