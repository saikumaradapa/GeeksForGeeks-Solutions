class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)

        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        # Sum of first k elements (the mandatory window)
        window_sum = prefix[k]
        ans = window_sum

        # max_prefix_extension tracks the best "extension" we can add
        # from the left side of the mandatory window.
        # At position i (0-indexed end of window), the mandatory window is arr[i-k+1..i]
        # and we can optionally extend left using a Kadane-like prefix.
        max_extend = 0

        for i in range(k, n):
            # Slide the mandatory window: add arr[i], remove arr[i-k]
            window_sum += arr[i] - arr[i - k]

            # max_extend represents the max sum subarray ending at arr[i-k]
            # that we can prepend to our window. We use Kadane's logic:
            # either extend the previous extension by arr[i-k], or start fresh at arr[i-k]
            max_extend = max(max_extend + arr[i - k], arr[i - k])

            # Answer is the best of: just the window, or window + left extension
            ans = max(ans, window_sum, window_sum + max_extend)

        return ans
