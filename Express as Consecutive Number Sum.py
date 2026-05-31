class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # n can be expressed as sum of 2+ consecutive positives
        # iff n is NOT a power of 2
        return (n & (n - 1)) != 0

'''
    math fact: n is sum of 2+ consecutive integers iff n is not a power of 2
    powers of 2 (1,2,4,8,...) cannot be expressed this way
    n & (n-1) == 0 means power of 2
    time complexity : O(1)
    space complexity : O(1)
'''
