class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        prev = arr[0]
        arr[0] = arr[0] ^ arr[1]
        for i in range(1, n - 1):
            temp = arr[i]
            arr[i] = prev ^ arr[i + 1]
            prev = temp
        arr[n - 1] = prev ^ arr[n - 1]

'''
    need original values for computation, so save previous element
    prev stores arr[i-1] before it was modified
    first and last are special cases (only one neighbor)
    time complexity : O(n)
    space complexity : O(1)
'''
