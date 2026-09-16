import bisect

class Solution:
    def dominantPairs(self, arr: list[int]) -> int:

        n = len(arr)
        half = n // 2
        left = arr[:half]
        right = arr[half:]

        # sort the right half; for each left element x, count how many
        # right elements y satisfy 5*y <= x  <=>  y <= x/5
        right.sort()

        count = 0
        for x in left:
            # largest value allowed for y is floor(x / 5)
            # count right elements <= x/5 via binary search
            # use bisect on the threshold: y such that 5*y <= x
            # find number of y with y <= x//5 handling negatives correctly:
            # condition is 5*y <= x  ->  y <= x/5 (real division)
            # bisect_right on x/5 works with floats
            idx = bisect.bisect_right(right, x / 5)
            count += idx

        return count
