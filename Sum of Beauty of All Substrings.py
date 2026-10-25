class Solution:
    def beautySum(self, s: str) -> int:
        """
        Track max and min frequency incrementally instead of scanning 26 counts.
        count_of_freq[f] = how many distinct chars currently have frequency f.

        Time:  O(n^2), O(1) work per extension
        Space: O(n), for count_of_freq
        """
        n = len(s)
        chars = [ord(c) - 97 for c in s]
        total = 0

        for i in range(n):
            freq = [0] * 26
            count_of_freq = [0] * (n + 2)
            max_freq = min_freq = 0

            for j in range(i, n):
                c = chars[j]
                old = freq[c]
                new = old + 1
                freq[c] = new

                if old:
                    count_of_freq[old] -= 1
                count_of_freq[new] += 1

                if new > max_freq:
                    max_freq = new

                if old == 0:
                    min_freq = 1            # a new char always has the lowest freq
                elif old == min_freq and count_of_freq[old] == 0:
                    min_freq = new          # last char at min moved up by one

                total += max_freq - min_freq

        return total
