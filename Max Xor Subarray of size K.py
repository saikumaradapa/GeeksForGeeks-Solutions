class Solution:
    def maxSubarrayXOR(self, arr, k):
        window_xor = 0
        max_xor = 0

        for i in range(k - 1):
            window_xor ^= arr[i]

        for r in range(k - 1, len(arr)):
            window_xor ^= arr[r]          # include new element
            max_xor = max(max_xor, window_xor)
            window_xor ^= arr[r - k + 1]  # exclude old element

        return max_xor

''' sliding window
    time complexity : O(n)
    space complexity : O(1)
'''
