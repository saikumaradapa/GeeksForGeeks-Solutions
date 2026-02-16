class Solution:
    def canAttend(self, arr):
        arr.sort()
        
        last = -1
        for start, end in arr:
            if start < last:
                return False
            last = max(end, last)
        
        return True

''' merge intervals approach 
    time complexity : O(n logn)
    space complexity : O(1)
'''
