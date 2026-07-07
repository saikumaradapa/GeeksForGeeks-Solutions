class Solution:
    def largestArea(self, n, m, arr):
        # blocked rows and columns
        rows = sorted(set(r for r, c in arr))
        cols = sorted(set(c for r, c in arr))

        # find max gap between consecutive blocked rows (including boundaries 0 and n+1)
        rows = [0] + rows + [n + 1]
        max_row_gap = 0
        for i in range(1, len(rows)):
            max_row_gap = max(max_row_gap, rows[i] - rows[i-1] - 1)

        # find max gap between consecutive blocked columns (including boundaries 0 and m+1)
        cols = [0] + cols + [m + 1]
        max_col_gap = 0
        for i in range(1, len(cols)):
            max_col_gap = max(max_col_gap, cols[i] - cols[i-1] - 1)

        return max_row_gap * max_col_gap
