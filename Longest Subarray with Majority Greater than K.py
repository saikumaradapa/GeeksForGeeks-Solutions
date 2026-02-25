class Solution:
    def longestSubarray(self, arr, k):
        
        n = len(arr)
        prefix = 0
        first_seen = {}
        max_len = 0
        
        for i in range(n):
            if arr[i] > k:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix > 0:
                max_len = i + 1
            
            if prefix - 1 in first_seen:
                max_len = max(max_len, i - first_seen[prefix - 1])
            
            if prefix not in first_seen:
                first_seen[prefix] = i
        
        return max_len
