import math

class Solution:
    def sameMod(self, arr):

        # k gives equal remainders for all elements iff k divides every pairwise
        # difference, i.e. k divides g = gcd(|arr[i] - arr[0]|)
        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

        if g == 0:            # all elements equal -> infinitely many k
            return -1

        # answer = number of positive divisors of g
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1 if i == g // i else 2
            i += 1

        return count
