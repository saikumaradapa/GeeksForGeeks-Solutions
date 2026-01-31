class Solution:
    def kthElement(self, a, b, k):
        n1, n2 = len(a), len(b)
        
        if n1 > n2:
            a, b = b, a
            n1, n2 = n2, n1
        
        # l - take ex n1 = 5, n2 = 6 and k = 7 you need atleast (k-n2) = 1 from a to left side 
        l, r = max(0, k-n2), min(n1, k)
        
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = k - mid1
            
            left1  = a[mid1-1] if mid1 > 0 else float('-inf')
            right1 = a[mid1]   if mid1 < n1 else float('inf')
            left2  = b[mid2-1] if mid2 > 0 else float('-inf')
            right2 = b[mid2]   if mid2 < n2 else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)

            elif left2 > right1:
                l = mid1 + 1
            else:
                r = mid1 - 1

''' optimal approach | binary search
    time complexity : O(log(min(n, m)))
    space complexity : O(1)
'''


##########################################################

class Solution:
    def kthElement(self, a, b, k):
        curr = 0
        id1, id2 = 0, 0
        n, m = len(a), len(b)

        for _ in range(k):
            if id1 < n and id2 < m and a[id1] <= b[id2]:
                curr = a[id1]
                id1 += 1
            elif id1 >= n:
                curr = b[id2]
                id2 += 1
            elif id2 >= m:
                curr = a[id1]
                id1 += 1
            else:
                curr = b[id2]
                id2 += 1

        return curr

''' two pointers approach 
    time complexity : O(k) | worst case O(n + m)
    space complexity : O(1)
'''


