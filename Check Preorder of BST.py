class Solution:
    def canRepresentBST(self, arr):
        stack = []
        lower = float('-inf')

        for x in arr:
            if x < lower:
                return False

            while stack and stack[-1] < x:
                lower = stack.pop()

            stack.append(x)

        return True
