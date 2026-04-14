class Solution:
    def removeSpaces(self, s):
        return s.replace(" ", "")


#########################################################################

class Solution:
    def removeSpaces(self, s):
        return ''.join([ch for ch in s if ch != ' '])


''' 
    time complexity : O(n)
    space complexity : O(n) # not possible in-place solution in python
'''
