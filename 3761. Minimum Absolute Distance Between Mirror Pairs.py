class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        res = float('inf')
        
        for i, num in enumerate(nums):
            
            if num in seen:
                res = min(res, i - seen[num])
            
            rev = int(str(num)[::-1])
            seen[rev] = i
        
        return res if res != float('inf') else -1

''' prefix sum
    time complexity : O(n)
    space complexity : O(n)
'''
