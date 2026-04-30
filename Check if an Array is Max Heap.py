class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if arr[i] < arr[left]:
                return False
            if right < n and arr[i] < arr[right]:
                return False
        return True

'''
    only internal nodes (indices 0 to n//2 - 1) can have children
    check each parent >= its children
    time complexity : O(n)
    space complexity : O(1)
'''
