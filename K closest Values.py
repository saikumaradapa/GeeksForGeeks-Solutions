class Solution:
    def getKClosest(self, root, target, k):
        """
        Returns k values in BST closest to the target.
        If two values have same absolute difference, choose the smaller one.
        
        Args:
            root (Node): Root node of BST.
            target (int): Target value.
            k (int): Number of closest values to return.
            
        Returns:
            List[int]: k closest values to target.
        Time Complexity: O(n)
        Auxiliary Space: O(n)
        """

        vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.data)
                inorder(node.right)

        inorder(root)

        # if abs diff same then take smaller value
        closest = sorted(
            vals,
            key=lambda x: (abs(x - target), x)
        )

        return closest[:k]
