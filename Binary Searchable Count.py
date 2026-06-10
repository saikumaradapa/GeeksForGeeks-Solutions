class Solution:
    def binarySearchable(self, arr):
        n = len(arr)
        count = 0
        for target in arr:
            l, r = 0, n - 1
            found = False
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    found = True
                    break
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if found:
                count += 1
        return count

'''
    simulate binary search for each element in the array
    if binary search finds it, it's binary searchable
    elements are distinct so no ambiguity
    time complexity : O(n log n)
    space complexity : O(1)
'''
