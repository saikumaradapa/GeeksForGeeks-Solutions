class Solution:
    def reducePairs(self, arr):
        stack = []
        for n in arr:
            alive = True
            # Collide when adjacent elements have opposite signs
            while alive and stack and ((stack[-1] > 0 and n < 0) or (stack[-1] < 0 and n > 0)):
                if abs(stack[-1]) < abs(n):
                    stack.pop()       # top is smaller, pop it, keep checking
                elif abs(stack[-1]) == abs(n):
                    stack.pop()       # equal, both die
                    alive = False
                else:
                    alive = False     # top is bigger, n dies
            if alive:
                stack.append(n)
        return stack

'''
    if two adjacent elements have opposite signs they collide
    bigger absolute value survives, equal values both die
    use stack, for each element keep colliding with stack top while opposite signs
    while loop handles chain reactions (winner keeps colliding backward)
    amortized O(n) — each element pushed and popped at most once
    time complexity : O(n)
    space complexity : O(n)
'''
