class Solution:
    def countAlwaysFound(self, arr):

        n = len(arr)

        # pref_max[i] = max of arr[0..i-1]  (everything strictly to the LEFT)
        pref_max = [float('-inf')] * n
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], arr[i - 1])

        # suf_min[i] = min of arr[i+1..n-1]  (everything strictly to the RIGHT)
        suf_min = [float('inf')] * n
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], arr[i + 1])

        count = 0
        for i in range(n):
            # always found iff bigger than ALL left elems and smaller than ALL right elems
            if arr[i] > pref_max[i] and arr[i] < suf_min[i]:
                count += 1

        return count
