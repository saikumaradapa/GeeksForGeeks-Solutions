class Solution:
    def findMinDiff(self, arr, M):
        
        n = len(arr)
        
        if M > n:
            return -1
        
        if M == 0:
            return 0
        
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
