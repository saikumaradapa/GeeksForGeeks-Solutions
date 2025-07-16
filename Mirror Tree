


class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if not root:
            return root
        
        left = self.mirror(root.left)
        right = self.mirror(root.right)
    
        root.left = right
        root.right = left 
        
        return root
