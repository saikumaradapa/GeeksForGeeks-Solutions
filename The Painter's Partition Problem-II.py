class Solution:
    def minTime(self, arr, k):
        
        def canPaint(maxTime):
            painters = 1
            total = 0
            
            for board in arr:
                if total + board <= maxTime:
                    total += board
                else:
                    painters += 1
                    total = board
                    
                    if painters > k:
                        return False
            return True
        
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if canPaint(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
