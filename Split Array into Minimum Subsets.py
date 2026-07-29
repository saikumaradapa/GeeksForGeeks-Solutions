class Solution:
    def minSubsets(self, arr):
        s = set(arr)
        count = 0
        for num in arr:
            # Count elements that start a new consecutive sequence
            if num - 1 not in s:
                count += 1
        return count
