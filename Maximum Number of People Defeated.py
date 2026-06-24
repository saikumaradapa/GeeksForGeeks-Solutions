class Solution:
    def maxPeopleDefeated(self, p):
        l, r = 1, p
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if (m * (m + 1) * (2 * m + 1)) // 6 <= p:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans


'''
    sum of 1² + 2² + ... + n² = n(n+1)(2n+1)/6
    binary search for largest n where sum <= p
    time complexity : O(log p)
    space complexity : O(1)
'''
