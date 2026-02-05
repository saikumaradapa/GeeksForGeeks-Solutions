class Solution:
    def maxOnes(self, arr, k):
        max_len = 0
        zeros = 0 
        
        l = 0 
        for r in range(len(arr)):
            if arr[r] == 0:
                zeros += 1
            
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len 

''' sliding window
    time complexity : O(n)
    space complexity : O(1)
'''
