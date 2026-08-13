class Solution:
    def maxDistance(self, V, src, edges):

        from collections import deque

        # Build adjacency list
        adj = [[] for _ in range(V)]
        indegree = [0] * V

        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1

        # Topological sort using Kahn's algorithm
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for nei, _ in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # Initialize distances with float('-inf')
        # The judge expects INT_MIN to map to "INF" display
        INT_MIN = float('-inf')
        dist = [INT_MIN] * V
        dist[src] = 0

        # Process in topological order
        for node in topo_order:
            if dist[node] == INT_MIN:
                continue
            for nei, w in adj[node]:
                if dist[node] + w > dist[nei]:
                    dist[nei] = dist[node] + w

        # Replace unreachable with integer INT_MIN that judge expects
        result = []
        for d in dist:
            if d == INT_MIN:
                result.append(-2**31)
            else:
                result.append(d)

        return result

''' time complexity : O(V + E)
    space complexity : O(V + E)
    approach to recall quickly

    - topological sort the DAG (Kahn's BFS)
    - initialize dist[src] = 0, all others -inf (unreachable)
    - process nodes in topological order
    - for each reachable node, relax all outgoing edges (maximize distance)
    - skip unreachable nodes
    - return -2^31 (INT_MIN in C++) for unreachable vertices as judge expects
'''
