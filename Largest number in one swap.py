class Solution:
    def largestSwap(self, s):
        s = list(s)
        
        # last occurrence of each digit
        last = {int(s[i]): i for i in range(len(s))}
        
        for i in range(len(s)):
            current = int(s[i])
            
            # check bigger digits from 9 down to current+1
            for d in range(9, current, -1):
                if d in last and last[d] > i:
                    j = last[d]
                    s[i], s[j] = s[j], s[i]
                    return "".join(s)
        
        return "".join(s)
