class Solution:
    def getCount(self, s, k):

        groups = [0] * 26                  # number of groups for each letter

        for i in range(len(s)):
            # a group starts at index 0 or wherever the character changes
            if i == 0 or s[i] != s[i - 1]:
                groups[ord(s[i]) - 97] += 1

        count = 0
        for g in groups:
            if g == k:
                count += 1
        return count
