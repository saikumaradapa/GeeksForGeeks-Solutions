class Solution:
    def minToggle(self, arr):
        n = len(arr)
        # for each split point i: left part [0..i-1] should be all 0s, right part [i..n-1] should be all 1s
        # cost = number of 1s in left + number of 0s in right

        # prefix count of 1s
        ones = [0] * (n + 1)
        for i in range(n):
            ones[i + 1] = ones[i] + arr[i]

        total_ones = ones[n]
        res = float('inf')

        # split at i: left = [0..i-1] all 0s, right = [i..n-1] all 1s
        for i in range(n + 1):
            ones_left = ones[i]           # 1s that need to become 0
            zeros_right = (n - i) - (total_ones - ones[i])  # 0s that need to become 1
            res = min(res, ones_left + zeros_right)

        return res

'''
    try every split point: left side all 0s, right side all 1s
    cost = 1s on left (toggle to 0) + 0s on right (toggle to 1)
    use prefix sum of 1s for O(1) per split
    time complexity : O(n)
    space complexity : O(n)
'''
