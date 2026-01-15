

class Solution:
    def catchThieves(self, arr, k):
        police = []
        thief = []
        n = len(arr)
        res = 0
        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thief.append(i)
        
        # Match police and thief
        p, t = 0, 0
        while p < len(police) and t < len(thief):
            # If within range, match
            if abs(police[p] - thief[t]) <= k:
                res += 1
                p += 1
                t += 1
            elif police[p] < thief[t]:
                p += 1
            else:
                t += 1
        return res
