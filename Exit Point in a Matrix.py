class Solution:
    def exitPoint(self, mat):
        n, m = len(mat), len(mat[0])
        # directions: right, down, left, up (clockwise)
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        d = 0  # start moving right
        r, c = 0, 0

        while 0 <= r < n and 0 <= c < m:
            if mat[r][c] == 1:
                mat[r][c] = 0
                d = (d + 1) % 4  # turn right
            r += dr[d]
            c += dc[d]

        # step back to get exit cell
        return [r - dr[d], c - dc[d]]
