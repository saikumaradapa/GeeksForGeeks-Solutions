class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:

        # each update j adds 1 to all indices >= j (1-based)
        # count how many updates start AT each index -> diff[j] (1-based)
        arr = [0] * n
        for j in updates:
            arr[j - 1] += 1            # mark +1 at the starting index (0-based)

        # a suffix contribution: an update at index p affects all i >= p,
        # so the value at index i = total updates with start <= i
        # build via prefix sum left to right
        running = 0
        for i in range(n):
            running += arr[i]
            arr[i] = running

        return arr
