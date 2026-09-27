from collections import defaultdict

class Solution:
    def longestPath(self, s, edges):

        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = s

        # iterative post-order (avoids recursion limit for deep trees)
        parent = [0] * (n + 1)
        order = []
        visited = [False] * (n + 1)
        st = [1]
        visited[1] = True
        while st:
            u = st.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    st.append(v)

        # downward chain states (u = topmost node of the chain, going strictly down):
        allR = [0] * (n + 1)   # longest ALL-RED  downward chain
        allB = [0] * (n + 1)   # longest ALL-BLUE downward chain
        rb   = [0] * (n + 1)   # longest R*B*     downward chain (reds then blues)
        br   = [0] * (n + 1)   # longest B*R*     downward chain (blues then reds)

        best = 1

        for u in reversed(order):
            cu = color[u - 1]
            childs = [c for c in adj[u] if c != parent[u]]

            if cu == 'R':
                allR[u] = 1
                allB[u] = 0
                rb[u]   = 1
                br[u]   = 1
                for c in childs:
                    if allR[c] + 1 > allR[u]: allR[u] = allR[c] + 1
                    if rb[c]   + 1 > rb[u]:   rb[u]   = rb[c]   + 1
                    if allR[c] + 1 > br[u]:   br[u]   = allR[c] + 1   # u=R stays in R-region
            else:  # 'B'
                allR[u] = 0
                allB[u] = 1
                rb[u]   = 1
                br[u]   = 1
                for c in childs:
                    if allB[c] + 1 > allB[u]: allB[u] = allB[c] + 1
                    if allB[c] + 1 > rb[u]:   rb[u]   = allB[c] + 1   # u=B -> blue below only
                    if br[c]   + 1 > br[u]:   br[u]   = br[c]   + 1

            best = max(best, allR[u], allB[u], rb[u], br[u])

            # top-2 (with index) of an array over children, so a "through" path uses
            # two DISTINCT child branches
            def top2(arr):
                b1 = b2 = 0
                i1 = -1
                for c in childs:
                    if arr[c] > b1:
                        b2 = b1; b1 = arr[c]; i1 = c
                    elif arr[c] > b2:
                        b2 = arr[c]
                return b1, b2, i1

            # Through path pivoting at u, read top->bottom as R*B*:
            # Case A: [all-red above (reversed)] + u + [R*B* below]        (u = R)
            #         [all-red above (reversed)] + u + [all-blue below]    (u = B)
            downA = rb if cu == 'R' else allB
            bAllR1, bAllR2, iAllR = top2(allR)
            bDA1, bDA2, iDA = top2(downA)
            if childs:
                if iAllR != iDA:
                    pairA = bAllR1 + bDA1
                else:
                    pairA = max(bAllR1 + bDA2, bAllR2 + bDA1)
                best = max(best, pairA + 1, bDA1 + 1, bAllR1 + 1)

            # Case B (u = B only): the R->B switch happens in the upper branch
            #   [B*R* above (reversed = R*B*)] + u + [all-blue below]
            if cu == 'B':
                bBR1, bBR2, iBR = top2(br)
                bAB1, bAB2, iAB = top2(allB)
                if childs:
                    if iBR != iAB:
                        pB = bBR1 + bAB1
                    else:
                        pB = max(bBR1 + bAB2, bBR2 + bAB1)
                    best = max(best, pB + 1, bBR1 + 1, bAB1 + 1)

        return best


