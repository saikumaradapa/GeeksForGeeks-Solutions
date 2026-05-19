from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        if start == end:
            return 0
        mod = 1000
        dist = [float('inf')] * mod
        q = deque([start])
        dist[start] = 0
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in arr:
                    val = (curr * nei) % mod
                    if ans < dist[val]:
                        dist[val] = ans
                        if val == end:
                            return ans
                        q.append(val)
        return -1

'''
    BFS on values mod 1000 (only 1000 possible states)
    multiply current by each arr element, take mod
    early exit when end is reached
    time complexity : O(1000 * n) where n = arr.size()
    space complexity : O(1000)
'''
