class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:

        n = len(arr)
        res = arr[:]
        i = 0
        # a swap is allowed only when the two adjacent values sum to EVEN, i.e. they
        # share parity. So an odd and an even can NEVER cross each other.
        # => within each MAXIMAL contiguous run of same-parity elements you can
        #    reorder freely; separate runs (split by opposite parity) can't mix.
        while i < n:
            j = i
            par = arr[i] & 1
            while j < n and (arr[j] & 1) == par:
                j += 1
            # sort this same-parity run descending for the lexicographically largest order
            res[i:j] = sorted(arr[i:j], reverse=True)
            i = j
        return res
