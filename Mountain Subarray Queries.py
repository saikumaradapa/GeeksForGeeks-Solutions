class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        # inc[i] = farthest index reachable by non-decreasing sequence from i
        inc = [0] * n
        inc[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i

        # dec[i] = leftmost index reachable by non-increasing sequence ending at i
        dec = [0] * n
        dec[0] = 0
        for i in range(1, n):
            if arr[i - 1] >= arr[i]:
                dec[i] = dec[i - 1]
            else:
                dec[i] = i

        ans = []
        for l, r in queries:
            ans.append(dec[r] <= inc[l])

        return ans
