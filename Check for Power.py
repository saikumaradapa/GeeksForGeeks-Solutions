class Solution:
    def isPower(self, x, y):
        if x == 1:
            return y == 1

        while y % x == 0:
            y //= x

        return y == 1

''' use division top-down instead of multiplication from down-top to avoid overflow
    time complexity : O(logₓ y)
    space complexity : O(1)
'''
