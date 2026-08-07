class Solution:
    def countFriendsPairings(self, n: int) -> int:

        if n <= 2:
            return n

        prev2 = 1  # f(1)
        prev1 = 2  # f(2)

        for i in range(3, n + 1):
            curr = prev1 + (i - 1) * prev2
            prev2 = prev1
            prev1 = curr

        return prev1

''' time complexity : O(n)
    space complexity : O(1)
    approach to recall quickly

    - nth person has two choices:
      1. stay single -> remaining n-1 people solve subproblem: f(n-1)
      2. pair with someone -> choose 1 of (n-1) partners, remaining n-2 solve: (n-1) * f(n-2)
    - recurrence: f(n) = f(n-1) + (n-1) * f(n-2)
    - base cases: f(1) = 1, f(2) = 2
    - use two variables to avoid array
'''
