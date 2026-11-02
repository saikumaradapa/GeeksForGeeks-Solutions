class Solution:
    def largestSumCycle(self, edge):

        n = len(edge)
        walk_id = [0] * n          # 0 = unvisited, otherwise id of the walk that reached it
        best = -1
        cur_id = 0

        for start in range(n):
            if walk_id[start]:
                continue           # already explored by an earlier walk
            cur_id += 1
            node = start
            # follow outgoing edges until a dead end or an already-visited cell
            while node != -1 and walk_id[node] == 0:
                walk_id[node] = cur_id
                node = edge[node]

            # reached a cell from THIS walk -> a new cycle starts at 'node'
            if node != -1 and walk_id[node] == cur_id:
                total = node
                nxt = edge[node]
                while nxt != node:
                    total += nxt
                    nxt = edge[nxt]
                if total > best:
                    best = total

        return best
