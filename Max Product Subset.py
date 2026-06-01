class Solution:
    def findMaxProduct(self, arr):
        n = len(arr)
        MOD = 10**9 + 7

        if n == 1:
            return arr[0]

        neg_count = 0
        zero_count = 0
        pos_count = 0
        max_neg = float('-inf')   # negative closest to zero

        for num in arr:
            if num > 0:
                pos_count += 1
            elif num < 0:
                neg_count += 1
                max_neg = max(max_neg, num)
            else:
                zero_count += 1

        if zero_count == n:
            return 0

        # only one negative, no positives, but zeros exist -> pick 0
        if neg_count == 1 and pos_count == 0 and zero_count > 0:
            return 0

        exclude_one = (neg_count % 2 == 1)
        ans = 1
        taken = 0
        for num in arr:
            if num == 0:
                continue
            if num < 0 and exclude_one and num == max_neg:
                exclude_one = False
                continue
            ans = (ans * num) % MOD
            taken += 1

        if taken == 0:
            return 0
        return ans % MOD

'''
    include all positives; include negatives in pairs
    if odd count of negatives, drop the one closest to zero (max_neg)
    decide exclusion BEFORE multiplying (can't divide after taking modulo)
    edge: all zeros -> 0; single lone negative with zeros -> 0
    time complexity : O(n)
    space complexity : O(1)
'''
