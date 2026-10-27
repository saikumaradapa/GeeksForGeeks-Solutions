class Solution:
    def getMaxWeight(self, s):

        n = len(s)
        # dp[i] = max weight of the prefix s[0..i-1]
        prev2 = 0          # dp[i-2]
        prev1 = 1          # dp[1]: a single character, unpaired

        if n == 1:
            return 1

        for i in range(2, n + 1):
            # option 1: s[i-1] stays unpaired (+1)
            single = prev1 + 1
            # option 2: pair s[i-2] with s[i-1]
            #   already different -> 4 ; same -> toggle one -> 4 - 1 = 3
            pair = prev2 + (4 if s[i - 1] != s[i - 2] else 3)

            cur = single if single > pair else pair
            prev2, prev1 = prev1, cur

        return prev1
