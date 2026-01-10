class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if n < k: return -1
        
        ans = -1
        l, r = max(arr), sum(arr)
        while l <= r:
            mid = (l + r) // 2
            students = self.required_students(arr, mid, k)
            if students <= k:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    def required_students(self, arr, limit, k):
        pages = arr[0]
        students = 1
        
        for i in range(1, len(arr)):
            if pages + arr[i] > limit:
                students += 1
                pages = arr[i]
            else:
                pages += arr[i]
        return students
        
''' Binary Search | minimize the maximum
    time complexity : O(log(sum - max + 1))
    space complexity : O(1)
'''
