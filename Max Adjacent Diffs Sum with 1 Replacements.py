class Solution:
    def maxDiffSum(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        keep, repl = 0, 0                     # dp for element 0 in each state
        for i in range(1, n):
            cur = arr[i]
            nkeep = max(keep + abs(cur - arr[i-1]), repl + abs(cur - 1))
            nrepl = max(keep + abs(1 - arr[i-1]), repl + abs(1 - 1))
            keep, repl = nkeep, nrepl
        return max(keep, repl)
