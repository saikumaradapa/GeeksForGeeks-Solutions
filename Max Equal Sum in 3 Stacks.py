class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        t1, t2, t3 = sum(s1), sum(s2), sum(s3)
        i = j = k = 0
        while not (t1 == t2 == t3):
            m = max(t1, t2, t3)
            if t1 == m:
                t1 -= s1[i]
                i += 1
            elif t2 == m:
                t2 -= s2[j]
                j += 1
            else:
                t3 -= s3[k]
                k += 1
            if i == len(s1) or j == len(s2) or k == len(s3):
                if t1 == t2 == t3:
                    return t1
                return 0
        return t1
