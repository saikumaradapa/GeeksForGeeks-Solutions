from collections import deque
class Solution:
    def bottomView(self, root):
        if not root: return []
        
        q = deque([(root, 0)])
        cols = {}
        
        while q:
            curr, cn = q.popleft()
            cols[cn] = curr.data
            
            if curr.left:
                q.append((curr.left, cn-1))
            if curr.right:
                q.append((curr.right, cn+1))
        
        res = []
        for i in range(min(cols.keys()), max(cols.keys())+1):
            res.append(cols[i])
        return res

''' 
    time complexity : O(n)
    space complexity : O(n)
'''
