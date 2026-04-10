class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n < 3:
            return []

        small = float('inf')
        mid = float('inf')

        # We need to track actual candidates for output
        # Use auxiliary arrays for O(1) extra beyond tracking
        s, m = 0, 0

        for i in range(n):
            if arr[i] <= small:
                small = arr[i]
                s = i
            elif arr[i] <= mid:
                mid = arr[i]
                m = i
            else:
                # arr[i] > mid > small, but s might be after m
                # We need a valid small that came before m
                # Find the smaller element before m
                for j in range(m):
                    if arr[j] < arr[m]:
                        return [arr[j], arr[m], arr[i]]
        return []
