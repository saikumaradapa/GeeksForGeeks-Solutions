import bisect
from collections import defaultdict

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:

        # Precompute positions of each character in s (sorted, ascending)
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        # check if 'word' is a subsequence of s using binary search over positions
        def is_subsequence(word):
            prev = -1                       # last matched index in s
            for ch in word:
                idx_list = pos.get(ch)
                if not idx_list:
                    return False
                # find the smallest index in idx_list that is > prev
                k = bisect.bisect_right(idx_list, prev)
                if k == len(idx_list):
                    return False            # no valid position left
                prev = idx_list[k]
            return True

        best = ""
        for word in d:
            # candidate must be longer, or same length but lexicographically smaller
            if (len(word) > len(best) or
                    (len(word) == len(best) and word < best)):
                if is_subsequence(word):
                    best = word

        return best
