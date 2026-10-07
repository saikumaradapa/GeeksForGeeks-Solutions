class Solution:
    def maxPathSum(self, root):

        self.best = float('-inf')

        def solve(node):
            # returns max downward sum from node to any leaf in its subtree
            if node.left is None and node.right is None:
                return node.data                     # leaf

            # recurse only into existing children
            if node.left and node.right:
                l = solve(node.left)
                r = solve(node.right)
                # leaf-to-leaf path bends through this node
                self.best = max(self.best, l + r + node.data)
                return max(l, r) + node.data

            # exactly one child: carry that side up (no bend here)
            child_sum = solve(node.left) if node.left else solve(node.right)
            return child_sum + node.data

        if root is None or (root.left is None and root.right is None):
            return -1                                # fewer than two leaves

        solve(root)
        return self.best if self.best != float('-inf') else -1
