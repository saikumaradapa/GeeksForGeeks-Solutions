import math

class Solution:
    def pairCount(self, x, y):

        # LCM must be a multiple of GCD, else no pair exists
        if y % x != 0:
            return 0

        # For gcd(a,b)=x and lcm(a,b)=y, write a=x*p, b=x*q with gcd(p,q)=1.
        # Then lcm = x*p*q = y  =>  p*q = y/x, and we need gcd(p,q)=1 (coprime).
        # Count ordered coprime pairs (p,q) with p*q = k.
        k = y // x

        count = 0
        i = 1
        while i * i <= k:
            if k % i == 0:
                j = k // i
                # (i, j) is a divisor pair with i*j = k
                if math.gcd(i, j) == 1:
                    # coprime -> valid; counts as 2 ordered pairs unless i == j
                    count += 1 if i == j else 2
            i += 1

        return count
