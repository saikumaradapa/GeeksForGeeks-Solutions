class Solution:
    def subarrayXor(self, arr, k):
        prefix = {0:1}
        xor = 0
        count = 0 
        
        for n in arr:
            xor = xor ^ n 
            x = xor ^ k 
            
            if x in prefix:
                count += prefix[x]
            
            prefix[xor] = prefix[xor] + 1 if xor in prefix else 1
        return count
        
''' 
    time complexity : O(n)
    space complexity : O(1)
'''
