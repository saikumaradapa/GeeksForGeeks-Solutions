class Solution:
    def findPosition(self, n):
        if n == 0 or (n & (n - 1)) != 0:
            return -1
        pos = 0
        while n > 1:
            n >>= 1
            pos += 1
        return pos + 1

'''
    n & (n-1) == 0 means exactly one set bit (power of 2)
    then just count shifts to find position
    time complexity : O(log n)
    space complexity : O(1)
'''


#######################################################################################################################

class Solution:
    def findPosition(self, n):
        res = -1
        for i in range(32):
            if (n >> i) & 1:
                if res != -1:
                    return -1
                res = i + 1
        return res

'''
    check each bit from LSB to MSB
    if a set bit is found and one was already found, return -1
    position is 1-indexed from LSB
    time complexity : O(log n)
    space complexity : O(1)
'''
