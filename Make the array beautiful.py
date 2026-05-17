class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []
        for n in arr:
            if stack and (stack[-1] < 0 and n >= 0 or stack[-1] >= 0 and n < 0):
                stack.pop()
            else:
                stack.append(n)
        return stack

'''
    stack: if top and current have different signs, pop (remove pair)
    otherwise push current
    similar to asteroid collision / parenthesis matching
    time complexity : O(n)
    space complexity : O(n)
'''
