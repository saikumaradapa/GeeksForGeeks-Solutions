class Solution:
    def getLastMoment(self, n, left, right):
        max_time = 0

        # Ants moving left
        if left:
            max_time = max(max_time, max(left))

        # Ants moving right
        if right:
            max_time = max(max_time, max(n - pos for pos in right))

        return max_time
