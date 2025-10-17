class Solution:
    def transformTree(self, root):
        self.sum = 0

        def reverse_inorder(node):
            if not node:
                return
            # visit right subtree first
            reverse_inorder(node.right)

            # update current node
            temp = node.data
            node.data = self.sum
            self.sum += temp

            # visit left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
