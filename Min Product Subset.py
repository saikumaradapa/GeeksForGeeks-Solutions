class Solution:
    def minProd(self, arr):

        count_neg = 0
        prod_all_nonzero = 1
        max_neg = None        # negative value closest to zero (smallest magnitude)
        min_overall = arr[0]  # fallback answer when there are no negatives

        for x in arr:
            if x < min_overall:
                min_overall = x
            if x == 0:
                continue
            if x < 0:
                count_neg += 1
                if max_neg is None or x > max_neg:
                    max_neg = x
            prod_all_nonzero *= x

        if count_neg == 0:
            return min_overall

        if count_neg % 2 == 1:
            return prod_all_nonzero
        else:
            return prod_all_nonzero // max_neg

''' time complexity : O(n)
    space complexity : O(1)
    approach to recall quickly

    - if no negatives exist: smallest single element wins (all factors >= 0,
      multiplying more only keeps/increases product), so answer = min(arr)
    - if negatives exist: multiply ALL nonzero elements together
        - odd count of negatives -> product already negative -> that's the min
        - even count of negatives -> product is positive, must drop exactly one
          negative to flip sign; drop the one CLOSEST TO ZERO (max value among
          negatives) since it loses the least magnitude
    - zeros are skipped entirely when negatives exist (a negative product always
      beats 0), only used as fallback when count_neg == 0
    - division by max_neg is always exact since it's a factor of the product
'''
