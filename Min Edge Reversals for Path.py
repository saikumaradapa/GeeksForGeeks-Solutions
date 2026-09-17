from collections import deque

class Solution:
    def minimumEdgeReversal(self, edges: list[list[int]], n: int, src: int, dst: int) -> int:

        # adjacency: (neighbor, cost)
        # forward edge u->v : cost 0 (use as-is)
        # reverse edge v->u : cost 1 (reverse this edge)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append((v, 0))   # traverse in original direction, free
            adj[v].append((u, 1))   # traverse against direction, costs 1 reversal

        INF = float('inf')
        dist = [INF] * (n + 1)
        dist[src] = 0
        dq = deque([src])

        # 0-1 BFS: 0-cost edges to the front, 1-cost edges to the back
        while dq:
            node = dq.popleft()
            d = dist[node]
            for nei, w in adj[node]:
                if d + w < dist[nei]:
                    dist[nei] = d + w
                    if w == 0:
                        dq.appendleft(nei)
                    else:
                        dq.append(nei)

        return dist[dst] if dist[dst] != INF else -1
