class Solution:
    def mergeTwoParts(self, arr):

        n = len(arr)

        # find the break point: first index where order drops (arr[i] < arr[i-1])
        bp = n
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                bp = i
                break

        if bp == n:
            return arr                      # already fully sorted

        # merge the two sorted parts arr[0:bp] and arr[bp:n] into a temp list
        left = arr[:bp]
        right = arr[bp:]
        i = j = idx = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[idx] = left[i]; i += 1
            else:
                arr[idx] = right[j]; j += 1
            idx += 1
        while i < len(left):
            arr[idx] = left[i]; i += 1; idx += 1
        while j < len(right):
            arr[idx] = right[j]; j += 1; idx += 1

        return arr
