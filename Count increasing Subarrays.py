class Solution:
    def countIncreasing(self, arr):
        res = 0
        l = 0
        
        for r in range(1, len(arr)):
            if arr[r] <= arr[r - 1]:
                l = r
            
            res += r - l
        
        return res

''' sliding window
    time complexity : O(n)
    space complexity : O(1)
'''

########################################################################################################################

class Solution:
    def countIncreasing(self, arr):
        res = 0
        length = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                length = 1
            
            res += length - 1
        
        return res

''' 
    time complexity : O(n)
    space complexity : O(1)
'''
