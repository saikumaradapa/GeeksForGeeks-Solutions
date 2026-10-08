class Solution:
    def maxFrequency(self, arr, k):

        arr.sort()
        n = len(arr)

        left = 0
        total = 0            # sum of the current window arr[left..right]
        best = 1

        for right in range(n):
            total += arr[right]

            # cost to raise every element in the window up to arr[right]:
            # arr[right] * window_size - total   (increments needed)
            # shrink while that cost exceeds k
            while arr[right] * (right - left + 1) - total > k:
                total -= arr[left]
                left += 1

            window = right - left + 1
            if window > best:
                best = window

        return best
