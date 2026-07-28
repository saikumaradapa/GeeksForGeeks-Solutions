from collections import deque

class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # 0-1 BFS on a modified graph:
        # Split each weight-2 edge into two weight-1 edges using a dummy node.
        # This gives us a graph with only weight-1 edges, solvable with plain BFS in O(V+E).

        # We'll use node IDs [0, V-1] for original nodes and V, V+1, ... for dummy nodes.
        adj = [[] for _ in range(V + len(edges))]  # worst case: one dummy per edge
        dummy = V

        for u, v, w in edges:
            if w == 1:
                adj[u].append(v)
                adj[v].append(u)
            else:  # w == 2, insert dummy node
                adj[u].append(dummy)
                adj[dummy].append(u)
                adj[dummy].append(v)
                adj[v].append(dummy)
                dummy += 1

        # BFS from src (all edges are weight 1 now)
        dist = [-1] * dummy
        dist[src] = 0
        queue = deque([src])

        while queue:
            node = queue.popleft()
            if node == dest:
                return dist[dest]
            for nei in adj[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    queue.append(nei)

        return -1
