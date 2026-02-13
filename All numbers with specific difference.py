class Solution:
    def getCount(self, n, d):
        
        def digitSum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        low, high = 1, n
        ans = n + 1   # default (not found)
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid - digitSum(mid) >= d:
                ans = mid
                high = mid - 1   # try smaller
            else:
                low = mid + 1    # need bigger
        
        if ans == n + 1:
            return 0
        
        return n - ans + 1
