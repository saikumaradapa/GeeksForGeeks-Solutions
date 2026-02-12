class Solution():
    def maxMinHeight(self, arr, k, w):
        n = len(arr)

        def canAchieve(target):
            added = [0] * (n + 1)
            curr_add = 0
            operations = 0

            for i in range(n):
                curr_add += added[i]

                if arr[i] + curr_add < target:
                    diff = target - (arr[i] + curr_add)
                    operations += diff

                    if operations > k:
                        return False

                    curr_add += diff
                    if i + w < n:
                        added[i + w] -= diff

            return True

        low = min(arr)
        high = min(arr) + k
        ans = low

        while low <= high:
            mid = (low + high) // 2

            if canAchieve(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
