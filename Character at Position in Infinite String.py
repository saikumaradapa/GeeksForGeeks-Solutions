class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        L = [len(s)]
        while L[-1] < pos:
            i = len(L)
            L.append(2 * L[-1] + i)
        i = len(L) - 1
        while i > 0:
            prev = L[i - 1]
            if pos <= prev:
                pass
            elif pos <= prev + i:
                return '$'
            else:
                pos = L[i] + 1 - pos
            i -= 1
        return s[pos - 1]
