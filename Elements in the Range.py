class Solution:
    def checkElements(self, start, end, arr):
        arr_set = set(arr)
        for n in range(start, end + 1):
            if n not in arr_set:
                return False
        return True

'''
    convert to set for O(1) lookup
    check every value in [start, end] exists
    time complexity : O(n + (end - start))
    space complexity : O(n) for the set
'''
