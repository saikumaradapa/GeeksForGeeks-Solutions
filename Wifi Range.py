class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                for j in range(max(i-x, 0), min(n-1, i+x)+1):
                    if s[j] == '1':
                        break
                else:
                    return False
        return True

'''
    for each room without wifi, check if any router within range x covers it
    brute force: check left and right within x distance
    time complexity : O(n * x)
    space complexity : O(1)
'''

#######################################################################################################

class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        # dist[i] = distance to nearest router
        # scan left to right: distance from last router on left
        # scan right to left: distance from nearest router on right
        # if min of both <= x for all i, return True

        left_dist = float('inf')
        right_dist = [float('inf')] * n

        # right to left pass
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                right_dist[i] = 0
            elif i + 1 < n:
                right_dist[i] = right_dist[i + 1] + 1

        # left to right pass
        for i in range(n):
            if s[i] == '1':
                left_dist = 0
            else:
                left_dist += 1
            if min(left_dist, right_dist[i]) > x:
                return False

        return True

'''
    compute distance to nearest router from left and right
    if min distance > x for any room, not covered
    time complexity : O(n)
    space complexity : O(n)
'''
