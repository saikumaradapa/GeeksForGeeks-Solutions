from heapq import heappop, heappush

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  # (distance, node)
        
        while heap:
            curr_dist, node = heappop(heap)
            
            # Skip stale entries
            if curr_dist > dist[node]:
                continue
            
            for adj, wt in graph[node]:
                new_dist = curr_dist + wt
                
                # Found shorter path
                if new_dist < dist[adj]:
                    dist[adj] = new_dist
                    ways[adj] = ways[node]
                    heappush(heap, (new_dist, adj))
                
                # Found another shortest path
                elif new_dist == dist[adj]:
                    ways[adj] = (ways[adj] + ways[node]) % MOD
        
        return ways[V-1] % MOD


''' Dijkstra + counting shortest paths.
    time complexity : O((V + E) log V)
    space complexity : O(V + E) 
'''
