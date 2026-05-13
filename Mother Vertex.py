class Solution:
    def findMotherVertex(self, V, edges):
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)

        visited = [False] * V
        order = []

        def dfs(node):
            stack = [(node, 0)]
            visited[node] = True
            while stack:
                u, idx = stack[-1]
                if idx < len(graph[u]):
                    stack[-1] = (u, idx + 1)
                    v = graph[u][idx]
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, 0))
                else:
                    stack.pop()
                    order.append(u)

        # step 1: get finish order
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # step 2: candidate = last finished
        candidate = order[-1]

        # step 3: verify
        visited = [False] * V
        visited[candidate] = True
        stack = [candidate]
        while stack:
            node = stack.pop()
            for adj in graph[node]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)

        if not all(visited):
            return -1

        # step 4: find smallest mother vertex
        # all vertices reachable from candidate are in its reachable set
        # any vertex that can reach candidate is also a mother vertex
        # use reverse graph: BFS from candidate on reverse graph
        rev_graph = [[] for _ in range(V)]
        for u, v in edges:
            rev_graph[v].append(u)

        # vertices that can reach candidate
        can_reach = [False] * V
        can_reach[candidate] = True
        stack = [candidate]
        while stack:
            node = stack.pop()
            for adj in rev_graph[node]:
                if not can_reach[adj]:
                    can_reach[adj] = True
                    stack.append(adj)

        # among those that can reach candidate, find smallest
        for i in range(V):
            if can_reach[i]:
                return i

        return candidate

''' Kosaraju's algorithm
    step 1: DFS to find last finished vertex (mother vertex candidate)
    step 2: verify candidate reaches all vertices
    step 3: find smallest vertex that can reach candidate (also a mother vertex)
    uses reverse graph to find all vertices that can reach candidate
    time complexity : O(V + E)
    space complexity : O(V + E)
'''
