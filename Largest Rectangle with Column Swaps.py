class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        max_area = 0
        # height[j] = consecutive 1s ending at current row in column j (running)
        height = [0] * m

        for i in range(n):
            # update running heights for this row
            for j in range(m):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0

            # counting sort of heights for this row (values range 0..n)
            cnt = [0] * (n + 1)
            for h in height:
                cnt[h] += 1

            # for a rectangle of height h, width = #columns with height >= h
            # (columns are freely reorderable, so just group the tallest together)
            cols_ge = 0
            for h in range(n, 0, -1):
                cols_ge += cnt[h]           # columns with height exactly h
                area = h * cols_ge          # cols_ge = columns with height >= h
                if area > max_area:
                    max_area = area

        return max_area

''' time complexity : O(n * (n + m))
    space complexity : O(n + m)   (heights + counting array; O(n*m) if you store full height matrix)
    approach to recall quickly

    - column swaps => columns can be arranged in ANY order
    - build histogram heights per row (consecutive 1s upward), like max-rect-in-histogram
    - since columns are reorderable, sort each row's heights descending;
      then the tallest columns can always be grouped side by side
    - for a chosen bar height h, the usable width = number of columns with height >= h
        area = h * (#columns with height >= h)   -> maximize over all h
    - use COUNTING SORT (heights are in 0..n) to hit O(n) per row instead of O(m log m):
        cnt[h] = columns with that height; sweep h from n down to 1 accumulating cols_ge
'''
