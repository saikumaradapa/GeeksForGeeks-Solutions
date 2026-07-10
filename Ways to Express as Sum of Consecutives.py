class Solution:
    def getCount(self, n):
        count = 0
        # sum of k consecutive starting from a: k*a + k*(k-1)/2 = n
        # so a = (n - k*(k-1)/2) / k
        # a must be a positive integer, so n - k*(k-1)/2 > 0 and divisible by k
        k = 2
        while k * (k - 1) // 2 < n:
            remainder = n - k * (k - 1) // 2
            if remainder % k == 0:
                count += 1
            k += 1
        return count
