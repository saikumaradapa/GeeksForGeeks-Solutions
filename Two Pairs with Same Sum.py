class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        groups = {}
        best = None
        for c in range(n):
            for d in range(c + 1, n):
                s = arr[c] + arr[d]
                lst = groups.get(s)
                if lst is None:
                    groups[s] = [(c, d)]
                    continue
                for a, b in lst:
                    if a != c and a != d and b != c and b != d:
                        cand = (a, b, c, d)
                        if best is None or cand < best:
                            best = cand
                        break
                lst.append((c, d))
        return list(best) if best else [-1, -1, -1, -1]
