from collections import defaultdict, deque
class Solution:
    def verticalSum(self, root):
        minc, maxc = 0, 0
        colSum = defaultdict(int)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            colSum[col] += node.data
            if node.left:
                q.append((node.left, col - 1))
                minc = min(minc, col - 1)
            if node.right:
                q.append((node.right, col + 1))
                maxc = max(maxc, col + 1)
        res = []
        for i in range(minc, maxc + 1):
            res.append(colSum[i])
        return res

'''
    BFS with column index: root=0, left=col-1, right=col+1
    sum values per column using defaultdict
    iterate from min column to max column for ordered output
    time complexity : O(n)
    space complexity : O(n)
'''
