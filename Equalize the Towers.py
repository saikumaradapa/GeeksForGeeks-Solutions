class Solution:
    def minCost(self, heights, cost):
        def computeCost(h):
            total = 0
            for i in range(len(heights)):
                total += abs(heights[i] - h) * cost[i]
            return total

        low = min(heights)
        high = max(heights)

        while low < high:
            mid = (low + high) // 2

            cost1 = computeCost(mid)
            cost2 = computeCost(mid + 1)

            if cost1 <= cost2:
                high = mid
            else:
                low = mid + 1

        return computeCost(low)
