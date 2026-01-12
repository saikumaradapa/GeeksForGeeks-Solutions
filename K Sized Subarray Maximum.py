from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()  # indices
        res = []

        for i in range(len(arr)):
            # Remove smaller elements from back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Remove elements out of window
            if dq[0] <= i - k:
                dq.popleft()

            # Window formed
            if i >= k - 1:
                res.append(arr[dq[0]])

        return res

''' monotonic deque
    time complexity : O(n)
    space complexity : O(k)
'''
