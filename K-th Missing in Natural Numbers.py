class Solution:
    def findKthSmall(self, arr, k):
        arr.sort()
        for x in arr:
            if x <= k:
                k += 1
            else:
                break
        return k
