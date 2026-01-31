class Solution:
    def rowWithMax1s(self, arr):
        n, m = len(arr), len(arr[0])
        max_row = -1
        j = m - 1
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                max_row = i 
                j -= 1
        return max_row

''' two pointers | optimal approach 
    time complexity : O(n + m)
    space complexity : O(1)
'''
