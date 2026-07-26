class Solution:
    def levelSort(self, arr):
        n = len(arr)
        result = []
        i = 0
        level_size = 1

        while i < n:
            # Extract nodes at this level
            level = arr[i:i + level_size]
            level.sort()
            result.append(level)
            i += level_size
            level_size *= 2

        return result
