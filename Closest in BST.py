
class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:

        best = float('inf')
        node = root

        while node:
            diff = abs(node.data - k)
            if diff < best:
                best = diff
            if diff == 0:
                return 0                 # can't do better than an exact match
            # BST property: move toward k
            node = node.left if k < node.data else node.right

        return best

''' time complexity : O(h)   (one root-to-leaf path)
    space complexity : O(1)  (iterative, no recursion stack)
    approach to recall quickly

    - follow the normal BST search path for k
    - at each node, update best = min(best, |node.data - k|)
    - go left if k < node.data, otherwise go right
    - nodes not on this path can't be closer: if k < node.data, everything in the
      right subtree is even larger than node.data, so it's farther from k
    - stop early on an exact match (difference 0)
    - verify: k=13 -> path 10 -> 11 -> best |11-13| = 2
              k=9  -> path 8 -> 9 -> 0
'''
