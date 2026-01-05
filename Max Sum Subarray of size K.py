class Solution:
    def maxSubarraySum(self, arr, k):
        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum

''' sliding window approach | two pointer approach
    time complexity : O(n)
    space complexity : O(1)
'''
