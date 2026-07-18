class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        n, m = len(matrix), len(matrix[0])

        suf = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                suf[i][j] = (
                    matrix[i][j]
                    + suf[i + 1][j]
                    + suf[i][j + 1]
                    - suf[i + 1][j + 1]
                )

        from functools import cache

        @cache
        def dfs(r, c, cuts):
            if suf[r][c] == 0:
                return 0
            if cuts == 1:
                return 1

            ans = 0

            # Horizontal cuts
            nr = r + 1
            while nr < n and suf[r][c] == suf[nr][c]:
                nr += 1
            while nr < n:
                ans = (ans + dfs(nr, c, cuts - 1)) % MOD
                nr += 1

            # Vertical cuts
            nc = c + 1
            while nc < m and suf[r][c] == suf[r][nc]:
                nc += 1
            while nc < m:
                ans = (ans + dfs(r, nc, cuts - 1)) % MOD
                nc += 1

            return ans

        return dfs(0, 0, k)
