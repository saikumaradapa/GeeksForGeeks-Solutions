class Solution:
    def absDiff(self, root):

        self.prev = None            # value of previously visited node (in-order)
        self.min_diff = float('inf')

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            # in a BST, in-order traversal yields values in sorted order,
            # so the closest values are always ADJACENT in this sequence
            if self.prev is not None:
                diff = node.data - self.prev
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev = node.data
            inorder(node.right)

        inorder(root)
        return self.min_diff
