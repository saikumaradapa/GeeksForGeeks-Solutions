class Solution:
    def getLastDigit(self, a, b):
        # edge case: b is "0" → a^0 = 1
        if b == "0":
            return 1

        # last digit of a
        last = int(a[-1])

        # b mod 4 (compute from string)
        b_mod4 = 0
        for ch in b:
            b_mod4 = (b_mod4 * 10 + int(ch)) % 4

        # if b_mod4 == 0 and b != "0", use 4 (cycle length)
        if b_mod4 == 0:
            b_mod4 = 4

        return pow(last, b_mod4) % 10
