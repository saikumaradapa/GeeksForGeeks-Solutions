from collections import deque
class Solution:
    def getCount(self, root, k):
        q = deque([root])
        cost = count = 0
        level = 1
        while q:
            if cost + level > k:      # can't afford this level or any deeper
                break
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    if cost + level <= k:
                        count += 1
                        cost += level
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return count
