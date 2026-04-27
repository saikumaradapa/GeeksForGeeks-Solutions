from collections import defaultdict
class Solution:
    def smallestSubstring(self, s):
        freq = defaultdict(int)
        
        l = 0 
        res = float('inf')
        for r in range(len(s)):
            freq[s[r]] += 1
            
            while s[l] not in ('0', '1', '2') or freq[s[l]] > 1:
                freq[s[l]] -= 1
                l += 1
            
            if freq['0'] > 0 and freq['1'] > 0 and freq['2'] > 0:
                res = min(res, r - l + 1)
        return res if res != float('inf') else -1
