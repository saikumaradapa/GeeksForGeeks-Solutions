class Solution:
    def balancePan(self, a, b):

        # Each power of a can go on the LEFT pan (+1), the RIGHT pan (-1), or be unused (0).
        # So b must be expressible in base a using only digits {-1, 0, 1}.
        # Walk base-a digits of b from least significant:
        while b > 0:
            r = b % a
            if r == 0:
                b //= a                 # digit 0: skip this power
            elif r == 1:
                b = (b - 1) // a        # digit +1: this power sits with b (left pan)
            elif r == a - 1:
                b = (b + 1) // a        # digit -1: borrow -> this power on the other pan
            else:
                return False            # digit not in {-1,0,1} -> impossible
        return True
