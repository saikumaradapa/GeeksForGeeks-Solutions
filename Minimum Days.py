class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:

        a = list(s)
        n = len(a)

        def bad(i):
            # pair (i, i+1) violates the rule
            return a[i] != '?' and a[i] == a[i + 1]

        cnt = 0
        for i in range(n - 1):
            if bad(i):
                cnt += 1

        if cnt == 0:
            return 0

        for day, idx in enumerate(p, start=1):
            # remove the pairs touching idx before changing it
            if idx > 0 and bad(idx - 1):
                cnt -= 1
            if idx < n - 1 and bad(idx):
                cnt -= 1
            a[idx] = '?'              # a '?' never forms a bad pair
            if cnt == 0:
                return day

        return n                      # unreachable: all '?' has no bad pairs
