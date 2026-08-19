class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:

        def count_at_most(x):
            # count triplets with sum <= x
            arr.sort()
            n = len(arr)
            count = 0
            for i in range(n - 2):
                lo = i + 1
                hi = n - 1
                while lo < hi:
                    if arr[i] + arr[lo] + arr[hi] <= x:
                        # all pairs (lo, lo+1..hi) are valid with this i and lo
                        count += (hi - lo)
                        lo += 1
                    else:
                        hi -= 1
            return count

        # triplets with sum in [l, r] = atMost(r) - atMost(l-1)
        return count_at_most(r) - count_at_most(l - 1)

''' time complexity : O(n^2)
    space complexity : O(1)  (in-place sort, ignoring sort's recursion stack)
    approach to recall quickly

    - reduce range count to two "at most" counts:
        answer = atMost(r) - atMost(l-1)
    - atMost(x): count triplets with sum <= x
        - sort the array
        - fix i, use two pointers lo=i+1, hi=n-1
        - if arr[i]+arr[lo]+arr[hi] <= x:
            every index between lo and hi pairs validly with lo -> add (hi - lo),
            then move lo forward
          else shrink hi
    - each fixed i does an O(n) two-pointer sweep -> O(n^2) total
'''
