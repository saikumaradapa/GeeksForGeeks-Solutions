class Solution:
    def derangeCount(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1

        prev2 = 0   # D(1)
        prev1 = 1   # D(2)

        for i in range(3, n + 1):
            curr = (i - 1) * (prev1 + prev2)
            prev2 = prev1
            prev1 = curr

        return prev1

''' use combinatorics recurrence D(n) = (n-1)*(D(n-1)+D(n-2))
    avoids brute force permutation generation
    time complexity : O(n)
    space complexity : O(1)
'''

###################################################################################################################

class Solution:
    def derangeCount(self, n: int) -> int:
        used = [False] * (n + 1)

        def backtrack(pos):
            # all positions filled
            if pos > n:
                return 1

            count = 0

            for num in range(1, n + 1):
                # skip if already used or fixed point
                if not used[num] and num != pos:
                    used[num] = True
                    count += backtrack(pos + 1)
                    used[num] = False

            return count

        return backtrack(1)

''' generate all permutations using backtracking while avoiding fixed positions
    time complexity : O(n!)
    space complexity : O(n)
'''
