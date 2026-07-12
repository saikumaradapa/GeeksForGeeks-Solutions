class Solution:
    def maxAmount(self, arr, k):
        MOD = 10**9 + 7
        arr.sort(reverse=True)
        arr.append(0)  # sentinel
        n = len(arr)
        res = 0

        for i in range(n - 1):
            # arr[0..i] all have same value arr[i]
            # next level is arr[i+1]
            count = i + 1  # number of sellers at current level
            diff = arr[i] - arr[i + 1]  # how many levels to drop

            if count * diff <= k:
                # sell all levels from arr[i] down to arr[i+1]+1
                # sum = count * (arr[i] + arr[i+1]+1) * diff / 2
                total = count * (arr[i] + arr[i+1] + 1) * diff // 2
                res = (res + total) % MOD
                k -= count * diff
            else:
                # can only partially fill
                full_levels = k // count
                remainder = k % count
                # sell 'full_levels' complete levels
                high = arr[i]
                low = arr[i] - full_levels + 1
                total = count * (high + low) * full_levels // 2
                res = (res + total) % MOD
                # sell 'remainder' tickets at next level
                res = (res + remainder * (arr[i] - full_levels)) % MOD
                k = 0
                break

        return res
