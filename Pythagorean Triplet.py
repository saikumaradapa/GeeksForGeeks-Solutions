class Solution:
    def pythagoreanTriplet(self, arr):
        
        max_val = max(arr)
        freq = [0] * (max_val + 1)
        
        for num in arr:
            freq[num] += 1
        
        for a in range(1, max_val + 1):
            if freq[a] == 0:
                continue
            
            for b in range(a, max_val + 1):
                if freq[b] == 0:
                    continue
                
                c2 = a*a + b*b
                c = int(c2 ** 0.5)
                
                if c <= max_val and c*c == c2 and freq[c] > 0:
                    if a == b == c and freq[a] < 3:
                        continue
                    if a == b and freq[a] < 2:
                        continue
                    return True
        
        return False
