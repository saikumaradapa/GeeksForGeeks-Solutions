class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        edge_cnt = 0 
        n = len(adj)
        for node in range(n):
            for adjNode in adj[node]:
                if node < adjNode:
                    edge_cnt += 1
        return edge_cnt
