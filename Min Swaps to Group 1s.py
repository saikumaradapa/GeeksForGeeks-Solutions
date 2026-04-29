class Solution:
    def minSwaps(self, arr):
        k = sum(arr)
        if k == 0:
            return -1
        
        curr = 0
        max_ones = 0
        l = 0
        
        for r in range(len(arr)):
            curr += arr[r]
            
            # maintain window size = k
            if r - l + 1 > k:
                curr -= arr[l]
                l += 1
            
            # valid window
            if r - l + 1 == k:
                max_ones = max(max_ones, curr)
        
        return k - max_ones
        
'''
    window size = count of 1s
    slide window, count 1s in each window
    min swaps = min zeros in any window of that size
    time complexity : O(n)
    space complexity : O(1)
'''
