class Solution:
    def countAtMostK(self, arr, k):
        freq = defaultdict(int)
        
        left = 0 
        res = 0
        dist_cnt = 0 
        
        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                dist_cnt += 1
            freq[arr[right]] += 1
            
            while dist_cnt > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    dist_cnt -= 1
                left += 1
            
            res += right - left + 1
        return res

''' 
    time complexity : O(n)
    space complexity : O(n)
'''
