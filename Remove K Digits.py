class Solution:
    def removeKdig(self, s, k):
        stack = []
        for digit in s:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # If still need to remove, pop from end
        while k > 0:
            stack.pop()
            k -= 1
        # Build result and remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
