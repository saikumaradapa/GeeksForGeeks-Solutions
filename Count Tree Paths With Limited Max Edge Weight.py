class Solution:
    def maximumWeight(self, n, edges, queries):

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            # iterative find with path halving
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        edges_sorted = sorted(edges, key=lambda e: e[2])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        res = [0] * len(queries)
        paths = 0
        ei = 0
        m = len(edges_sorted)

        for qi in order:
            x = queries[qi]
            # add every edge allowed by this query
            while ei < m and edges_sorted[ei][2] <= x:
                u, v, _ = edges_sorted[ei]
                ru, rv = find(u), find(v)
                if ru != rv:
                    paths += size[ru] * size[rv]   # new paths crossing this edge
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
                ei += 1
            res[qi] = paths

        return res
