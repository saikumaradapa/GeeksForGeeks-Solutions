from collections import defaultdict, deque
class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        indegree = [0] * n
        graph = defaultdict(list)
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1

        finish = [0] * n
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
                finish[node] = duration[node]

        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for adj in graph[node]:
                finish[adj] = max(finish[adj], finish[node] + duration[adj])
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        if visited < n:      # cycle -> not all nodes processed
            return -1
        return max(finish)
