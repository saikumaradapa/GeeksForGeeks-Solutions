from collections import defaultdict
class Solution:
    def countSubstr (self, s, k):
        return self.at_most(s, k) - self.at_most(s, k - 1)

    def at_most(self, s, k):
        freq = defaultdict(int)
        dist_char = 0
        res = 0
        
        l = 0 
        for r in range(len(s)):
            if freq[s[r]] == 0:
                dist_char += 1
            freq[s[r]] += 1
            
            while dist_char > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    dist_char -= 1
                l += 1
            res += r - l + 1
        return res

''' sliding window approach
    time complexity : O(n)
    space complexity : O(n)
'''
