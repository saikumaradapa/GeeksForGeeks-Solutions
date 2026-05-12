class Solution:
    def palindromePair(self, arr):
        word_map = {}
        for i, w in enumerate(arr):
            word_map[w] = i

        n = len(arr)
        for i in range(n):
            word = arr[i]
            l = len(word)
            for j in range(l + 1):
                left = word[:j]
                right = word[j:]

                # case 1: left is palindrome, reverse of right exists at different index
                if left == left[::-1]:
                    rev_right = right[::-1]
                    if rev_right in word_map and word_map[rev_right] != i:
                        return True

                # case 2: right is palindrome, reverse of left exists at different index
                if j != l and right == right[::-1]:
                    rev_left = left[::-1]
                    if rev_left in word_map and word_map[rev_left] != i:
                        return True

        return False

'''
    for each word, split into left + right at every position
    if left is palindrome and reverse(right) exists at different index → pair
    if right is palindrome and reverse(left) exists at different index → pair
    use dict with index to handle duplicates correctly
    j != l check in case 2 avoids double counting empty right at j=l
    
    example: ["g", "g"] → split "g" at j=0: left="", right="g"
      left "" is palindrome, rev_right="g" exists at different index → True
    
    time complexity : O(n * l^2)
    space complexity : O(n * l)
'''
