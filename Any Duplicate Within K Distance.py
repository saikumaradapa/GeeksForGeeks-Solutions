class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:

        window = set()                 # values among the last k elements
        for i, x in enumerate(arr):
            if x in window:
                return True            # same value within distance k
            window.add(x)
            if len(window) > k:
                window.remove(arr[i - k])   # drop the element now too far back
        return False

''' time complexity : O(n)
    space complexity : O(min(n, k))   (set holds at most k values)
    approach to recall quickly

    - sliding window of the previous k elements, kept in a set
    - for each x: if x is already in the window -> duplicate within k -> True
    - otherwise add x, and once the window has more than k values,
      remove arr[i - k] (it's now more than k positions behind the next index)
    - the window never holds duplicates (we'd have returned True),
      so the set size always equals the window length
    - verify: [1,5,4,5,1], k=3 -> 5 seen at index 1, again at 3 -> True
              [10,2,3,4,10,5], k=3 -> 10 dropped before index 4 -> False
'''
