class Solution:
    def maxOnes(self, arr):
        """
        Intuition:
        ----------
        We are allowed to flip at most one contiguous subarray.
        Flipping changes:
            0 -> 1  (gain +1)
            1 -> 0  (loss -1)

        So instead of thinking about flipping directly, we convert the problem into:
            "Find a subarray that gives maximum net gain"

        Transform the array into a gain array:
            gain = +1 if element == 0
            gain = -1 if element == 1

        Now the problem becomes:
            Find the maximum subarray sum (Kadane's Algorithm)

        Final answer:
            total_ones (already present)
            + max_gain (best improvement from flipping)

        Edge case:
            If all elements are 1 → flipping reduces count,
            so max_gain = 0 → we simply return total_ones

        Time Complexity:
            O(n) → single pass

        Space Complexity:
            O(1) → no extra space used
        """

        total_ones = sum(arr)

        max_gain = 0   # best gain seen so far
        curr = 0       # current subarray gain

        for x in arr:
            gain = 1 if x == 0 else -1

            # Kadane's choice:
            # start new subarray OR extend existing one
            curr = max(gain, curr + gain)

            # track best gain
            max_gain = max(max_gain, curr)

        return total_ones + max_gain
