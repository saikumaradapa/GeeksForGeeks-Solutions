class Solution:
    def URLify(self, s): 
        return "".join([ch if ch != " " else "%20" for ch in s])

'''
    time complexity : O(n)
    space complexity : O(n) | not possible to do inplace in python
'''
