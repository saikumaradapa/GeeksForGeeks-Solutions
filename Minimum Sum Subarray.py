class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:

        # Kadane's algorithm, flipped to find the MINIMUM-sum subarray
        cur_min = arr[0]      # min-sum subarray ending at current index
        best = arr[0]         # global minimum

        for i in range(1, len(arr)):
            # either start fresh at arr[i], or extend the previous min-ending subarray
            cur_min = min(arr[i], cur_min + arr[i])
            if cur_min < best:
                best = cur_min

        return best
