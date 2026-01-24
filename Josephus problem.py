class Solution:
    def josephus(self, n, k):
        ans = 0  # f(1, k) = 0 (0-based)
        
        for i in range(2, n + 1):
            ans = (ans + k) % i
        
        return ans + 1  # convert to 1-based
