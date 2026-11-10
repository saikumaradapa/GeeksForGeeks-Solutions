class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:

        count = {}
        for x in arr:
            count[x] = count.get(x, 0) + 1
            # the first element to reach k occurrences is the answer
            if count[x] == k:
                return x
        return -1

''' time complexity : O(n)
    space complexity : O(n)   (counts for distinct values)
    approach to recall quickly

    - scan left to right, counting how often each value has appeared so far
    - the moment a count hits k, that element's k-th occurrence is the earliest
      of any element, so return it immediately
    - no count reaches k -> return -1
    - k = 1 -> the first element is returned
    - verify: [1,7,4,3,4,8,7], k=2 -> 4 hits 2 at index 4 (before 7 at index 6) -> 4
              [10,8,2], k=10 -> -1
'''
