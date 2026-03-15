from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []

        q = deque([(root, 0)])
        col_map = defaultdict(list)
        min_col = max_col = 0

        while q:
            node, col = q.popleft()
            col_map[col].append(node.data)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        return [col_map[c] for c in range(min_col, max_col + 1)]

  ''' BFS
      time complexity : O(n)
      space complexity : O(n)
  '''
