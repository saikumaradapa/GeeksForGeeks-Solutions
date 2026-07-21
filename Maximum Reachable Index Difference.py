class Solution:
    def maxIndexDifference(self, s):
        n = len(s)

        best = [-1] * 26
        reach = [0] * n

        ans = -1

        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')

            reach[i] = i
            if c < 25 and best[c + 1] != -1:
                reach[i] = best[c + 1]

            best[c] = max(best[c], reach[i])

            if c == 0:
                ans = max(ans, reach[i] - i)

        return ans
