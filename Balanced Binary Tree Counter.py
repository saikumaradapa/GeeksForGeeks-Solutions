class Solution:
    def countBT(self, h: int) -> int:

        MOD = 10**9 + 7

        prev2 = 1    # f(0): empty tree
        prev1 = 1    # f(1): single node

        for _ in range(2, h + 1):
            # both subtrees h-1, or one h-1 and one h-2 (two orders)
            cur = (prev1 * prev1 + 2 * prev1 * prev2) % MOD
            prev2, prev1 = prev1, cur

        return prev1

''' time complexity : O(h)
    space complexity : O(1)
    approach to recall quickly

    - a tree of height h = root + left and right subtrees whose heights
      differ by at most 1, and the taller one has height h-1
    - subtree height choices:
        (h-1, h-1)                  -> f(h-1) * f(h-1)
        (h-1, h-2) or (h-2, h-1)    -> 2 * f(h-1) * f(h-2)
    - f(h) = f(h-1)^2 + 2*f(h-1)*f(h-2)
    - base: f(0) = 1 (empty tree), f(1) = 1 (single node)
    - keep only the last two values -> O(1) space; take mod each step
    - verify: f(2) = 1 + 2*1*1 = 3 ; f(3) = 9 + 2*3*1 = 15
'''
