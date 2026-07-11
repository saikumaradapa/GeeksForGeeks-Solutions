class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n, m = len(mat), len(mat[0])
        self.ans = -1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, length):
            if r == xd and c == yd:
                self.ans = max(self.ans, length)
                return
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    mat[nr][nc] = 0  # mark visited
                    dfs(nr, nc, length + 1)
                    mat[nr][nc] = 1  # backtrack

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        mat[xs][ys] = 0  # mark source visited
        dfs(xs, ys, 0)
        mat[xs][ys] = 1
        return self.ans
