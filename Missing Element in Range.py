class Solution:
    def missingRange(self, arr, low, high):
        mem = set(arr)
        return [num for num in range(low, high + 1) if num not in mem]

''' 
    time complexity : O(n + (high - low + 1))
    space complexity : O(n)
'''
    
