class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:

        n = len(arr)
        window = min(m, n)   # can't visit more trees than exist

        # sliding window of size 'window' over a circular array
        # first window: indices 0 .. window-1
        cur = sum(arr[:window])
        best = cur

        # slide the window start from 1 to n-1 (wrapping around)
        for start in range(1, n):
            # remove the element leaving the window (the old start)
            cur -= arr[start - 1]
            # add the new element entering (wraps with modulo)
            cur += arr[(start + window - 1) % n]
            if cur > best:
                best = cur

        return best

