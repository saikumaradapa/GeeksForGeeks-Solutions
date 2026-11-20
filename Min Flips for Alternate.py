class Solution:
    def minFlips(self, s):
        mismatch = 0
        for i, c in enumerate(s):
            if int(c) != i % 2:
                mismatch += 1
        return min(mismatch, len(s) - mismatch)
