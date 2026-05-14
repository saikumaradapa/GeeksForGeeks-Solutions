class Solution:
    def search(self, a, b):
        n, m = len(a), len(b)
        res = []

        # KMP: build failure function for b
        lps = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and b[k] != b[i]:
                k = lps[k - 1]
            if b[k] == b[i]:
                k += 1
            lps[i] = k

        # search
        j = 0
        for i in range(n):
            while j > 0 and b[j] != a[i]:
                j = lps[j - 1]
            if b[j] == a[i]:
                j += 1
            if j == m:
                res.append(i - m + 1)
                j = lps[j - 1]

        return res

'''
    KMP pattern matching on integer arrays
    build LPS (failure function) for pattern b
    scan array a, use LPS to avoid re-checking matched prefixes
    time complexity : O(n + m)
    space complexity : O(m)
'''
