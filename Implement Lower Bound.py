class Solution:
    def lowerBound(self, arr, target):
        low, high = 0, len(arr) - 1
        res = len(arr)
        
        while low <= high:
            mid = (low + high) // 2 
            if arr[mid] >= target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
            
