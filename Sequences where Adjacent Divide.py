class Solution:
    def count(self, n: int, m: int) -> int:
        # dp[j] = number of valid arrays of current length ending with value j
        dp = [1] * (m + 1)  # length 1: one array for each value 1..m

        for _ in range(n - 1):
            new_dp = [0] * (m + 1)
            for val in range(1, m + 1):
                # Count transitions: all values that divide val or are multiples of val
                # Divisors of val
                d = 1
                while d * d <= val:
                    if val % d == 0:
                        new_dp[val] += dp[d]
                        if d != val // d:
                            new_dp[val] += dp[val // d]
                    d += 1
                # Multiples of val (excluding val itself, already counted as divisor)
                mult = 2 * val
                while mult <= m:
                    new_dp[val] += dp[mult]
                    mult += val
            dp = new_dp

        return sum(dp[1:])
