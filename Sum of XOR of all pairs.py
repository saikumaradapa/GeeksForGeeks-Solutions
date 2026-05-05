class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        res = 0
        for bit in range(20):
            c = 0
            for num in arr:
                if (num >> bit) & 1:
                    c += 1
            res += c * (n - c) * (1 << bit)
        return res

'''
    for each bit position, count set bits (c) and unset (n-c)
    XOR is 1 only when bits differ → c * (n-c) pairs contribute at that bit
    multiply by bit value (1 << bit)
    
    example: arr = [7, 3, 5] → 111, 011, 101
      bit 0 (val=1): c=3, n-c=0 → 3*0*1 = 0  (all same, no XOR difference)
      bit 1 (val=2): c=2, n-c=1 → 2*1*2 = 4  (pairs 7,5 and 3,5 differ)
      bit 2 (val=4): c=2, n-c=1 → 2*1*4 = 8  (pairs 7,3 and 5,3 differ)
      total = 0 + 4 + 8 = 12 ✓
    
    time complexity : O(n * 20) = O(n)
    space complexity : O(1)
'''
