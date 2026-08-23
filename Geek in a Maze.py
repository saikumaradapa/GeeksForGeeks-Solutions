from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        # starting cell is an obstacle
        if mat[r][c] == '#':
            return 0

        INF = float('inf')
        # dist[i][j] = minimum number of UP moves needed to reach (i, j)
        dist = [[INF] * m for _ in range(n)]
        dist[r][c] = 0

        # 0-1 BFS: an UP move costs 1 (uses up-budget), everything else costs 0
        dq = deque([(r, c)])

        while dq:
            i, j = dq.popleft()
            base = dist[i][j]

            # (di, dj, weight)
            for di, dj, w in ((-1, 0, 1), (1, 0, 0), (0, -1, 0), (0, 1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] != '#':
                    nd = base + w
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if w == 0:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))

        # count reachable cells that respect both budgets
        count = 0
        for i in range(n):
            for j in range(m):
                up_used = dist[i][j]
                if up_used == INF:
                    continue
                # for any path to row i:  up_used - down_used = r - i  (fixed)
                # => down_used = up_used + (i - r)
                down_used = up_used + (i - r)
                if up_used <= u and down_used <= d:
                    count += 1

        return count

''' time complexity : O(n * m)   (0-1 BFS; log factor only if Dijkstra is used)
    space complexity : O(n * m)
    approach to recall quickly

    - left/right moves are FREE, only vertical moves are budgeted (u up, d down)
    - KEY invariant: for ANY path to a cell in row i,
          up_used - down_used = r - i     (each up -1 row, each down +1 row)
      so up_used and down_used differ by a constant -> minimizing one minimizes both
    - therefore feasibility is single-objective: find MIN up_used per cell
    - 0-1 BFS from (r,c): up move = weight 1, down/left/right = weight 0
      (push weight-0 neighbors to front, weight-1 to back)
    - a cell (i,j) is visitable iff:
          up_used <= u   AND   down_used = up_used + (i - r) <= d
    - count all reachable cells satisfying both bounds
'''
