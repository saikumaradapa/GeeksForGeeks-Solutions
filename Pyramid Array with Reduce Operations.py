class Solution:
    def formPyramid(self, arr):

        n = len(arr)

        # left[i] = tallest pyramid height at i if the LEFT slope (1,2,3,...) ends here
        # bounded by the stone height arr[i] and by left[i-1] + 1 (slope rises by 1)
        left = [0] * n
        left[0] = min(arr[0], 1)
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        # right[i] = tallest pyramid height at i if the RIGHT slope (...,3,2,1) starts here
        right = [0] * n
        right[n - 1] = min(arr[n - 1], 1)
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        total = sum(arr)
        best_cost = total                      # worst case: reduce everything to 0

        for i in range(n):
            # peak at i must satisfy BOTH slopes -> min of the two
            peak = min(left[i], right[i])
            if peak == 0:
                continue
            kept = peak * peak                 # 1+2+...+peak+...+2+1 = peak^2
            cost = total - kept                # everything not kept is reduced away
            if cost < best_cost:
                best_cost = cost

        return best_cost
