class Solution:
    def searchInsertK(self, arr, k):
        n = len(arr)
        for i in range(n):
            if arr[i] >= k:
                return i
        return n

''' 
    time complexity : O(n)
    space complexity : O(1)
'''
