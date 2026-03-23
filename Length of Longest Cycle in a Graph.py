class Solution:
    def longestCycle(self, V, edges):
        
        adj = [-1] * V
        for u, v in edges:
            adj[u] = v
        
        visited = [False] * V
        ans = -1
        
        for i in range(V):
            
            if visited[i]:
                continue
            
            curr = i
            step = 0
            seen = {}
            
            while curr != -1 and not visited[curr]:
                
                visited[curr] = True
                seen[curr] = step
                step += 1
                curr = adj[curr]
                
                if curr in seen:
                    ans = max(ans, step - seen[curr])
                    break
        
        return ans
