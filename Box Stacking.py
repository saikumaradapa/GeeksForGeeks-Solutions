class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:

        # Step 1: generate all 3 rotations of every box.
        # Normalize the base so base dimensions are (smaller, larger); the third
        # dimension is the height. 3 rotations per box (each dimension as height).
        boxes = []
        n = len(height)
        for i in range(n):
            dims = sorted([height[i], width[i], length[i]])   # [a, b, c], a<=b<=c
            a, b, c = dims
            # base (a,b) height c ; base (a,c) height b ; base (b,c) height a
            boxes.append((a, b, c))   # base a*b, height c
            boxes.append((a, c, b))   # base a*c, height b
            boxes.append((b, c, a))   # base b*c, height a

        # Step 2: sort by base AREA descending (larger base must go below)
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

        m = len(boxes)
        # dp[i] = max stack height with box i on top of the stack
        dp = [b[2] for b in boxes]     # at least the box's own height

        best = 0
        # Step 3: LIS-style O(m^2) DP
        for i in range(m):
            for j in range(i):
                # box i can go ABOVE box j only if BOTH base dims strictly smaller
                if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                    if dp[j] + boxes[i][2] > dp[i]:
                        dp[i] = dp[j] + boxes[i][2]
            if dp[i] > best:
                best = dp[i]

        return best
