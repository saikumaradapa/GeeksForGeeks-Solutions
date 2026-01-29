from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26        # frequency of a-z
        q = deque()            # to maintain order
        result = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            # Remove all repeating chars from front
            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            # First non-repeating or '#'
            if q:
                result.append(q[0])
            else:
                result.append('#')

        return "".join(result)
