class Solution:
    def countSubsets(self, arr):
        MOD = 10**9 + 7

        # Since arr[i] <= 30, primes up to 30 are: 2,3,5,7,11,13,17,19,23,29
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        # For each value 1..30, precompute its prime bitmask
        # If a value has a repeated prime factor, it's "invalid" (can't be in any valid subset)
        prime_idx = {p: i for i, p in enumerate(primes)}

        def get_mask(val):
            """Returns bitmask of prime factors if square-free, else -1."""
            if val == 1:
                return 0  # contributes no primes
            mask = 0
            for i, p in enumerate(primes):
                if val % p == 0:
                    val //= p
                    if val % p == 0:
                        return -1  # repeated prime factor
                    mask |= (1 << i)
            if val > 1:
                return -1  # shouldn't happen since val <= 30
            return mask

        # Precompute masks for values 1..30
        val_mask = {}
        for v in range(1, 31):
            val_mask[v] = get_mask(v)

        # Count occurrences of each value
        from collections import Counter
        freq = Counter(arr)

        # Count of 1s — each subset of 1s can be combined with any valid product subset
        ones_count = freq.get(1, 0)
        # Number of non-empty subsets of 1s: 2^ones_count - 1
        # Multiplier for combining with other subsets: 2^ones_count (include any subset of 1s)
        ones_multiplier = pow(2, ones_count, MOD)

        # DP with bitmask: dp[mask] = number of ways to choose elements (excluding 1s)
        # such that product's prime factorization corresponds exactly to 'mask'
        # We only need non-zero masks for final answer (product of one or more distinct primes)

        # 10 primes, so 2^10 = 1024 states
        dp = [0] * 1024
        dp[0] = 1  # empty subset

        # Process each value > 1 with valid mask
        for val in range(2, 31):
            mask = val_mask[val]
            if mask == -1 or freq.get(val, 0) == 0:
                continue
            cnt = freq[val]

            # Each occurrence of this value can either be included or not,
            # but if included, its bits must not overlap with current mask.
            # Since multiple copies of same value exist, and each has same mask,
            # including more than one would repeat primes. So we can include at most one.
            # But different indices count as different subsets, so including any ONE of the
            # cnt copies gives cnt ways.

            # Process in reverse to avoid using same value group twice in one pass
            new_dp = dp[:]
            for prev_mask in range(1024):
                if dp[prev_mask] == 0:
                    continue
                if prev_mask & mask:
                    continue  # overlapping primes
                new_mask = prev_mask | mask
                new_dp[new_mask] = (new_dp[new_mask] + dp[prev_mask] * cnt) % MOD
            dp = new_dp

        # Sum all dp[mask] for mask > 0 (product must have at least one prime)
        result = 0
        for mask in range(1, 1024):
            result = (result + dp[mask]) % MOD

        # Each such subset can be combined with any subset of 1s (including empty set of 1s)
        result = result * ones_multiplier % MOD

        # Also count subsets that are purely 1s? No — product of only 1s is 1,
        # which is NOT a product of one or more distinct primes.

        return result
