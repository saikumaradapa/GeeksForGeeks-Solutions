class Solution:
    def findIndex(self, s):
        n = len(s)
        close_right = sum(1 for ch in s if ch == ')')
        open_left = 0
        for i in range(n):
            if open_left == close_right:
                return i
            if s[i] == '(':
                open_left += 1
            else:
                close_right -= 1
        if open_left == close_right:
            return n
        return 0

'''
    open_left = count of '(' before position i
    close_right = count of ')' from position i to end
    as we scan: '(' adds to open_left, ')' leaves close_right
    check equality at each position
    time complexity : O(n)
    space complexity : O(1)
'''
