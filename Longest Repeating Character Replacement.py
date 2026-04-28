from collections import defaultdict

class Solution:
    def longestSubstr(self, s, k):
        freq = defaultdict(int)
        
        l = 0
        res = 0
        maxf = 0   # max frequency in window
        
        for r in range(len(s)):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])
            
            # shrink if invalid
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

''' 
    time complexity : O(n)
    space complexity : O(1)
'''
