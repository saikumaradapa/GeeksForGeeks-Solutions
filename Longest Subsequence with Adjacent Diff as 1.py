class Solution:
    def longestSubseq(self, arr):

        # best[v] = length of the longest valid subsequence ending with value v
        best = {}
        ans = 0

        for x in arr:
            # extend the best subsequence ending in x-1 or x+1, whichever is longer
            prev = max(best.get(x - 1, 0), best.get(x + 1, 0))
            best[x] = prev + 1
            if best[x] > ans:
                ans = best[x]

        return ans
