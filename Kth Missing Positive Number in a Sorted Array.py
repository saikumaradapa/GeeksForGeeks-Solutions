class Solution:
    def kthMissing(self, arr, k):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # missing(i) = arr[i] - (i + 1)
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        # (left existing) + (k missing) = left + k
        return left + k


''' 
    time complexity : O(logn)
    space complexity : O(1)
'''

######################################################3

class Solution:
    def kthMissing(self, arr, k):
        curr_num = 1
        curr_miss_count = 0
        idx = 0

        while idx < len(arr):
            if curr_num == arr[idx]:
                curr_num += 1
                idx += 1
            else:
                curr_miss_count += 1
                if curr_miss_count == k:
                    return curr_num
                curr_num += 1

        # If kth missing is beyond the last array element
        return arr[-1] + (k - curr_miss_count)

''' 
    time complexity : O(n)
    space complexity : O(1)
'''
