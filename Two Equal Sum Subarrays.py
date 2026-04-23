class Solution:
    def canSplit(self, arr):
        total_sum = sum(arr)

        # early pruning
        if total_sum % 2 != 0:
            return False

        curr_sum = 0
        target = total_sum // 2

        for num in arr:
            curr_sum += num
            if curr_sum == target:
                return True

        return False

''' check if prefix sum equals half of total sum
    if total sum is odd, split is impossible
    time complexity : O(n)
    space complexity : O(1)
'''
