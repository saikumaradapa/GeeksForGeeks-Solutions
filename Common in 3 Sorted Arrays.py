class Solution:
    def commonElements(self, a, b, c):
        p1, p2, p3 = 0, 0, 0
        res = []
        while p1 < len(a) and p2 < len(b) and p3 < len(c):
            if a[p1] == b[p2] == c[p3]:
                if not res or res[-1] != a[p1]:
                    res.append(a[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            elif a[p1] < b[p2]:
                p1 += 1
            elif b[p2] < c[p3]:
                p2 += 1
            else:
                p3 += 1
        return res

'''
    three pointers, one per array
    if all equal, add to result (skip duplicates via res[-1] check)
    otherwise advance the pointer with the smallest value
    time complexity : O(n1 + n2 + n3)
    space complexity : O(1) excluding output
'''
