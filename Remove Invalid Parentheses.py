class Solution:
    def validParenthesis(self, s):
        # find min removals needed
        left_rem = 0
        right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = set()

        def dfs(i, left_count, right_count, left_rem, right_rem, curr):
            if i == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(curr)
                return

            ch = s[i]

            if ch == '(' and left_rem > 0:
                dfs(i + 1, left_count, right_count, left_rem - 1, right_rem, curr)
            if ch == ')' and right_rem > 0:
                dfs(i + 1, left_count, right_count, left_rem, right_rem - 1, curr)

            if ch == '(':
                dfs(i + 1, left_count + 1, right_count, left_rem, right_rem, curr + ch)
            elif ch == ')':
                if left_count > right_count:
                    dfs(i + 1, left_count, right_count + 1, left_rem, right_rem, curr + ch)
            else:
                dfs(i + 1, left_count, right_count, left_rem, right_rem, curr + ch)

        dfs(0, 0, 0, left_rem, right_rem, "")
        return sorted(res)

'''
    first count min '(' and ')' to remove
    backtrack: at each char, either remove it (if removals left) or keep it
    keep ')' only if left_count > right_count (valid so far)
    use set to avoid duplicates, sort result lexicographically
    time complexity : O(2^n)
    space complexity : O(n) recursion depth
'''
