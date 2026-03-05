from collections import defaultdict

class Solution:
    def longestKSubstr(self, s, k):
        freq = defaultdict(int)
        l = 0
        res = -1
        
        for r, ch in enumerate(s):
            freq[ch] += 1
            
            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            if len(freq) == k:
                res = max(res, r - l + 1)
        
        return res

''' sliding window + frequency map
    time complexity : O(n)
    space complexity : O(26)
'''
