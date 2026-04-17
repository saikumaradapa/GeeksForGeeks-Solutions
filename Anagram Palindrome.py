class Solution:
    def canFormPalindrome(self, s):
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        
        odd = 0
        for c in cnt:
            if c % 2:
                odd += 1
                if odd > 1:
                    return False
        return True

''' count method
    time complexity : O(n)
    space complexity : O(1)
'''

############################################################################################################################

class Solution:
    def canFormPalindrome(self, s):
        mask = 0
        
        for ch in s:
            mask ^= (1 << (ord(ch) - ord('a')))
        
        return mask == 0 or (mask & (mask - 1)) == 0

''' same as above but here
    Each bit represents a character
    XOR toggles:
    even → 0
    odd → 1
    At the end:
    mask == 0 → all even
    mask has only 1 bit set → one odd
'''
