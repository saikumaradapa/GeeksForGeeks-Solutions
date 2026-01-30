from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        stack = []

        # Step 1: Push first half into stack
        for _ in range(half):
            stack.append(q.popleft())

        # Step 2: Enqueue back stack elements
        while stack:
            q.append(stack.pop())

        # Step 3: Move first half (original second half) to back
        for _ in range(half):
            q.append(q.popleft())

        # Step 4: Again push first half into stack
        for _ in range(half):
            stack.append(q.popleft())

        # Step 5: Interleave
        while stack:
            q.append(stack.pop())  # from first half
            q.append(q.popleft())  # from second half

        return q
