

from collections import deque
class Solution:
    
    def levelOrder(self,root):
        q = deque([root])
        res = []
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                if node:
                    
                    level.append(node.data)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.extend(level)
        return res

''' time complexity : O(n)
    space complexity : O(n)
'''
