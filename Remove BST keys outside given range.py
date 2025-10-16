class Solution:
    def removekeys(self, root, l, r):
        """
        Removes all the nodes in the BST whose values lie outside the range [l, r].
        The modified tree should remain a valid BST.

        Args:
        root (Node): The root of the BST.
        l (int): The lower bound of the range.
        r (int): The upper bound of the range.

        Returns:
        Node: The root of the modified BST.

        Time Complexity: (O(n))
        Space Complexity: (O(h))        
                
        """
        # Base case: If the root is None, return None
        if not root:
            return None
        
        # If the current node's value is less than l, 
        # then all nodes of the left subtree are outside the range
        if root.data < l:
            return self.removekeys(root.right, l, r)
        
        # If the current node's value is greater than r, 
        # then all nodes of the right subtree are outside the range
        if root.data > r:
            return self.removekeys(root.left, l, r)
        
        # If the current node is in the range [l, r], process its subtrees
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)

        return root
