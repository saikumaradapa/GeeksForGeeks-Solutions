class Solution:
    def minOperation(self, n):

        ops = 0
        # work BACKWARDS from n to 0:
        #   if n is even -> last op was a doubling, so undo it: n //= 2
        #   if n is odd  -> last op was +1, so undo it: n -= 1
        while n > 0:
            if n % 2 == 0:
                n //= 2       # reverse of "double"
            else:
                n -= 1        # reverse of "+1"
            ops += 1

        return ops
