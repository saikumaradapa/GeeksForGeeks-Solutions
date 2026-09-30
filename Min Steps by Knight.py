from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:

        # convert 1-based positions to 0-based for grid indexing
        sr, sc = knightPos[0] - 1, knightPos[1] - 1
        tr, tc = targetPos[0] - 1, targetPos[1] - 1

        if (sr, sc) == (tr, tc):
            return 0

        # 8 knight moves
        moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                 (-1, -2), (-1, 2), (1, -2), (1, 2)]

        visited = [[False] * n for _ in range(n)]
        visited[sr][sc] = True
        q = deque([(sr, sc, 0)])   # (row, col, distance)

        while q:
            r, c, d = q.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if nr == tr and nc == tc:
                        return d + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

        
        return -1   # target unreachable (only possible on tiny/edge boards)
