class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:

        # Bellman-Ford. Use a virtual source: initialize all dist to 0
        # (equivalent to adding a 0-weight edge from a super-source to every vertex),
        # so a negative cycle in ANY component gets detected.
        dist = [0] * V

        # Relax all edges V-1 times
        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break   # no changes -> no negative cycle possible

        # One more pass: if any edge can still relax, a negative cycle exists
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True

        return False

''' time complexity : O(V * E)
    space complexity : O(V)
    approach to recall quickly

    - use Bellman-Ford to detect a negative weight cycle
    - init ALL dist[] = 0 (virtual super-source with 0-weight edge to every node)
      so cycles in any disconnected component are still reachable/detected
    - relax every edge (V-1) times (early exit if a full pass makes no update)
    - do ONE extra relaxation pass:
        if any edge can STILL be relaxed (dist[u] + w < dist[v]),
        a negative weight cycle exists -> return True
    - otherwise return False
'''
