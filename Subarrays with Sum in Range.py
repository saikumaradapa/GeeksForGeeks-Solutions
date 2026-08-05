class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # Count subarrays with sum <= x using sliding window
        # Since all elements are positive, we can use this approach
        def count_at_most(x):
            if x < 0:
                return 0
            count = 0
            window_sum = 0
            left = 0
            for right in range(len(arr)):
                window_sum += arr[right]
                while window_sum > x:
                    window_sum -= arr[left]
                    left += 1
                # All subarrays ending at 'right' with start in [left, right] are valid
                count += (right - left + 1)
            return count

        # Subarrays with sum in [l, r] = atMost(r) - atMost(l-1)
        return count_at_most(r) - count_at_most(l - 1)
