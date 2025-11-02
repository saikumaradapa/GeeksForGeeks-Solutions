from collections import deque
class Solution:
    def maxWidth(self, root):
        q = deque([root])
        max_width = 0 
        while q:
            count = 0 
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    count += 1
                    q.append(curr.left)
                    q.append(curr.right)
            max_width = max(max_width, count)
        return max_width

''' 
    time complexity : O(n)
    space complexity : O(n) - max no. of nodes in a level
'''
