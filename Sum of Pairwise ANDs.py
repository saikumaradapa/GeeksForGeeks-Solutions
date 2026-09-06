class Solution:
    def pairAndSum(self, arr):

        total = 0
        # arr[i] <= 1e8 < 2^27, so 27 bits are enough (use 32 to be safe)
        for bit in range(32):
            # count how many numbers have this bit set
            count = 0
            mask = 1 << bit
            for x in arr:
                if x & mask:
                    count += 1
            # any pair where BOTH numbers have this bit set contributes 2^bit
            # number of such pairs = C(count, 2)
            total += (count * (count - 1) // 2) * mask

        return total
