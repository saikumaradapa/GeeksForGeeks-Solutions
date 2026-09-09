class Solution:
    def findMax(self, n):
        if n < 10:
            return n

        s = str(n)
        best = n
        best_sum = self.get_digit_sum(n)

        # for each position, reduce that digit by 1 and set the rest to 9
        for i in range(len(s)):
            if s[i] == '0':
                continue
            # candidate: keep prefix, reduce s[i] by 1, fill rest with 9
            cand = int(s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1))
            if cand <= 0:
                continue
            cs = self.get_digit_sum(cand)
            # max digit sum; on tie prefer the larger number
            if cs > best_sum or (cs == best_sum and cand > best):
                best_sum = cs
                best = cand

        return best

    def get_digit_sum(self, num):
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        return digit_sum
