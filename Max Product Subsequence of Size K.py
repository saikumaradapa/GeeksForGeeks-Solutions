class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:

        NEG_INF = float('-inf')
        POS_INF = float('inf')

        # dpmax[j] / dpmin[j] = max / min product of a subsequence of EXACTLY j elements
        dpmax = [NEG_INF] * (k + 1)
        dpmin = [POS_INF] * (k + 1)
        dpmax[0] = 1
        dpmin[0] = 1

        for x in arr:
            # iterate j downward -> each element used at most once (0/1 knapsack)
            for j in range(k, 0, -1):
                if dpmax[j - 1] != NEG_INF:
                    a = dpmax[j - 1] * x
                    b = dpmin[j - 1] * x
                    hi = a if a > b else b
                    lo = a if a < b else b
                    if hi > dpmax[j]:
                        dpmax[j] = hi
                    if lo < dpmin[j]:
                        dpmin[j] = lo

        return dpmax[k]
