Problem Link : https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/1


class Solution:
    def intersection(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        res = []

        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                res.append(a[i])
                
                # Skip duplicates in both arrays
                val = a[i]
                while i < n and a[i] == val:
                    i += 1
                while j < m and b[j] == val:
                    j += 1

        return res
        
''' two pointers 
    time complexity : O(n + m)
    space complexity : O(1) # ignoring output 
'''

##################################################################################################################################################################################################################


class Solution:
    #Function to return a list containing the intersection of two arrays.
    def intersection(self, arr1, arr2):
        seen = set(arr1)
        
        result = []
        for n in arr2:
            if n in seen:
                result.append(n)
                seen.remove(n)
        return result
        
''' time complexity : O(n + m)
    space complexity : O(n)

    The membership test 'if n in seen' takes 𝑂(1) on average due to the hash table implementation of sets.
'''                    
