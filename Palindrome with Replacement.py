class Solution:
    def minimumSum(self, s: str) -> int:

        n = len(s)
        a = list(s)

        # Step 1: enforce the palindrome constraint on each mirror pair (i, n-1-i)
        i, j = 0, n - 1
        while i <= j:
            ci, cj = a[i], a[j]
            if ci != '?' and cj != '?':
                if ci != cj:
                    return -1              # two fixed letters disagree -> impossible
            elif ci == '?' and cj != '?':
                a[i] = cj                  # copy the known partner
            elif ci != '?' and cj == '?':
                a[j] = ci
            # both '?' -> leave free, decide in step 2
            i += 1
            j -= 1

        # Step 2: fill remaining '?' runs to minimize sum of adjacent ASCII diffs
        res = a[:]
        k = 0
        while k < n:
            if res[k] != '?':
                k += 1
                continue
            # maximal run of '?' spanning [k, m-1]
            m = k
            while m < n and res[m] == '?':
                m += 1
            left = res[k - 1] if k - 1 >= 0 else None     # known letter on the left
            right = res[m] if m < n else None             # known letter on the right

            if left is None and right is None:
                fill = 'a'                                # whole string free -> all same
                for t in range(k, m):
                    res[t] = fill
            elif left is None:
                for t in range(k, m):                     # only right known -> match it (0 cost)
                    res[t] = right
            elif right is None:
                for t in range(k, m):                     # only left known -> match it (0 cost)
                    res[t] = left
            else:
                # both known: set run flat to 'left' -> interior diffs 0, single jump |left-right|
                for t in range(k, m):
                    res[t] = left
            k = m

        # keep it a palindrome (mirrored runs have mirrored neighbors, so this is consistent)
        for p in range(n // 2):
            res[n - 1 - p] = res[p]

        total = 0
        for p in range(n - 1):
            total += abs(ord(res[p]) - ord(res[p + 1]))
        return total
