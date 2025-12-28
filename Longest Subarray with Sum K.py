class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefixSum = dict()
        max_len = 0 
        sum = 0 
        
        for i in range(len(arr)):
            sum += arr[i]
            if sum == k:
                max_len = max(max_len, i + 1)
            
            rem = sum - k 
            if rem in prefixSum:
                max_len = max(max_len, i - prefixSum[rem])
            
            prefixSum[sum] = i if sum not in prefixSum else prefixSum[sum]
        
        return max_len
        
''' prefix sum approach | works for both +ve and -ve nums
    time complexity : O(n)
    space complexity : O(n)
'''

###########################################################################################################################################################


class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum = 0 
        max_len = 0 
        
        l = 0 
        for r in range(len(arr)):
            sum += arr[r]
            
            while l < r and sum > k:
                sum -= arr[l]
                l += 1
            
            if sum == k:
                max_len = max(max_len, r - l + 1)
        
        return max_len
        
''' sliding window approach | works for only for +ve nums
    time complexity : O(n)
    space complexity : O(1)
'''
