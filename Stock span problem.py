class Solution:
    def calculateSpan(self, arr):
        stack = []   # stores indices
        span = [0] * len(arr)

        for i in range(len(arr)):
            # Remove elements smaller than or equal to current
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack empty, span is entire range till i
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push current index
            stack.append(i)

        return span
