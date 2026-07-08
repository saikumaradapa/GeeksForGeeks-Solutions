class Solution:
    def countCoordinates(self, mat):
        from collections import deque
        n, m = len(mat), len(mat[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(starts):
            visited = [[False]*m for _ in range(n)]
            q = deque()
            for r, c in starts:
                visited[r][c] = True
                q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                        # reverse flow: neighbor can reach boundary if its value >= current
                        if mat[nr][nc] >= mat[r][c]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
            return visited

        # Station P: top row + left column
        p_starts = []
        for c in range(m):
            p_starts.append((0, c))
        for r in range(1, n):
            p_starts.append((r, 0))

        # Station Q: bottom row + right column
        q_starts = []
        for c in range(m):
            q_starts.append((n-1, c))
        for r in range(n-1):
            q_starts.append((r, m-1))

        reach_p = bfs(p_starts)
        reach_q = bfs(q_starts)

        count = 0
        for r in range(n):
            for c in range(m):
                if reach_p[r][c] and reach_q[r][c]:
                    count += 1
        return count
