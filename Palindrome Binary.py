class Solution:
    def isBinaryPalindrome(self, n):
        b = bin(n)[2:]
        return b == b[::-1]

'''
    convert to binary string, check if it equals its reverse
    time complexity : O(log n)
    space complexity : O(log n)
'''
