class Solution:
    def isBitSet(self, n):
        if n == 0:
            return False
        return n & (n + 1) == 0

'''
    if all bits are set, n = 2^k - 1, so n+1 = 2^k (single bit)
    n & (n+1) == 0 only when n is all 1s
    handle n=0 separately (no bits set)
    time complexity : O(1)
    space complexity : O(1)
'''
