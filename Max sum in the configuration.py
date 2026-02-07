class Solution:
    def maxSum(self, arr):
        n = len(arr)
        arrSum = sum(arr)

        # Compute R0
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]

        maxVal = currVal

        # Compute subsequent values
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)

        return maxVal
