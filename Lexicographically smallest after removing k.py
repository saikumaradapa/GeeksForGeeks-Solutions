class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # correct k
        if n & (n - 1) == 0:   # n is a power of 2
            k = k // 2
        else:
            k = k * 2

        # can't remove k chars, or result would be empty
        if k >= n or k < 0:
            return -1

        # monotonic increasing stack: remove larger chars when a smaller one comes
        stack = []
        to_remove = k
        for ch in s:
            while stack and to_remove > 0 and stack[-1] > ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)

        # if removals remain, trim from the end (largest at end of increasing seq)
        if to_remove > 0:
            stack = stack[:-to_remove]

        result = "".join(stack)
        return result if result else -1

'''
    step 1: correct k — if n is power of 2, halve it; else double it
    if k >= n, can't remove that many → -1
    step 2: monotonic stack, pop larger chars when smaller char arrives (greedy)
    if removals remain after pass, trim from the end
    n & (n-1) == 0 checks power of 2
    time complexity : O(n + k)
    space complexity : O(n)
'''
