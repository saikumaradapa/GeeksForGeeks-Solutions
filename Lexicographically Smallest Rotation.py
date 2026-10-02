class Solution:
    def lexiString(self, s: str) -> str:
        """
        Booth's algorithm: find start index of lexicographically smallest rotation.

        Time:  O(n)
        Space: O(n)

        Work on s+s so every rotation is a length-n window. f[] is a KMP-like
        failure array. k tracks the best candidate start. On mismatch, skip
        ahead using f to avoid re-comparing shared prefixes (the O(n^2) trap).
        """
        s2 = s + s
        n = len(s2)
        f = [-1] * n          # failure function
        k = 0                 # least-rotation start index so far

        for j in range(1, n):
            ch = s2[j]
            i = f[j - k - 1]
            while i != -1 and ch != s2[k + i + 1]:
                if ch < s2[k + i + 1]:
                    k = j - i - 1
                i = f[i]
            if ch != s2[k + i + 1]:      # i == -1
                if ch < s2[k]:           # ch < s2[k + i + 1] with i=-1
                    k = j
                f[j - k] = -1
            else:
                f[j - k] = i + 1

        return s2[k:k + len(s)]
