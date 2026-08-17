from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):

        num_cells = n * n
        move = [-1] * (num_cells + 1)   # move[i] = final cell after snake/ladder at i, -1 if none

        for i in range(0, len(lad), 2):
            move[lad[i]] = lad[i + 1]

        for i in range(0, len(sn), 2):
            move[sn[i]] = sn[i + 1]

        visited = [False] * (num_cells + 1)
        queue = deque()
        queue.append((1, 0))   # (cell, throws)
        visited[1] = True

        while queue:
            cell, throws = queue.popleft()

            if cell == num_cells:
                return throws

            for die in range(1, 7):
                nxt = cell + die
                if nxt > num_cells:
                    break
                if move[nxt] != -1:
                    nxt = move[nxt]
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append((nxt, throws + 1))

        return -1

''' time complexity : O(n^2)
    space complexity : O(n^2)
    approach to recall quickly

    - classic BFS shortest path on a graph of n*n cells
    - each cell i connects to i+1 .. i+6 (dice throw), capped at board size
    - precompute move[] array: if a cell is the start of a snake/ladder,
      redirect to its endpoint immediately (this happens BEFORE marking visited,
      since landing triggers the jump automatically)
    - BFS guarantees shortest number of throws (unweighted graph, level = throws)
    - return throws when we pop the destination cell, else -1 if queue exhausted
'''
