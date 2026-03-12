class Solution:
    def kBitFlips(self, arr, k):
        
        n = len(arr)
        flipped = [0] * n
        flip = 0
        ans = 0
        
        for i in range(n):
            
            if i >= k:
                flip ^= flipped[i-k]
            
            if arr[i] ^ flip == 0:
                
                if i + k > n:
                    return -1
                
                ans += 1
                flip ^= 1
                flipped[i] = 1
        
        return ans
