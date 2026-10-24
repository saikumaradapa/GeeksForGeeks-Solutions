class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:

        r = c = 0                    # displacement from the start cell
        min_r = max_r = 0
        min_c = max_c = 0

        for ch in s:
            if ch == 'L':
                c -= 1
            elif ch == 'R':
                c += 1
            elif ch == 'D':
                r -= 1
            else:                    # 'U'
                r += 1

            if r < min_r: min_r = r
            if r > max_r: max_r = r
            if c < min_c: min_c = c
            if c > max_c: max_c = c

        # the walk occupies (max - min + 1) rows/cols; it must fit inside the grid
        return (max_r - min_r + 1) <= n and (max_c - min_c + 1) <= m
