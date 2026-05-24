class Solution:
    def coin(self, arr):
        l, r = 0, len(arr) - 1
        while l != r:
            if arr[l] <= arr[r]:
                r -= 1
            else:
                l += 1
        return arr[l]

'''
    greedy: always pick larger end (remove it)
    two pointers shrink from whichever end is larger
    last remaining = arr[l] when l == r
    time complexity : O(n)
    space complexity : O(1)
'''
