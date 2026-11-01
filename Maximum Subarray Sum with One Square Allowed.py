class Solution:
    def maximumSubarray(self, arr: list[int]) -> int:

        # no_sq = best sum of a subarray ending here, nothing squared
        # sq    = best sum of a subarray ending here, exactly one element squared
        no_sq = arr[0]
        sq = arr[0] * arr[0]
        best = max(no_sq, sq)

        for i in range(1, len(arr)):
            x = arr[i]
            x2 = x * x
            # square x now: start fresh at x^2, or extend a no-square run with x^2
            # or keep a run where the square was used earlier, and add x as is
            new_sq = max(x2, no_sq + x2, sq + x)
            new_no = max(x, no_sq + x)
            no_sq, sq = new_no, new_sq
            if sq > best:
                best = sq
            if no_sq > best:
                best = no_sq

        return best
