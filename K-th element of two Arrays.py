class Solution:
    def kthElement(self, a, b, k):
        if len(a) > len(b):
            return self.kthElement(b, a, k)  # Ensure a is the smaller array
        
        n, m = len(a), len(b)
        low, high = max(0, k - m), min(k, n)
        
        while low <= high:
            cutA = (low + high) // 2
            cutB = k - cutA
            
            leftA = a[cutA - 1] if cutA > 0 else float('-inf')
            leftB = b[cutB - 1] if cutB > 0 else float('-inf')
            rightA = a[cutA] if cutA < n else float('inf')
            rightB = b[cutB] if cutB < m else float('inf')
            
            # Check if the partition is correct
            if leftA <= rightB and leftB <= rightA:
                return max(leftA, leftB)
            elif leftA > rightB:
                high = cutA - 1
            else:
                low = cutA + 1


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

''' 
    time complexity : O(k) | worst case O(n + m)
    space complexity : O(1)
'''


